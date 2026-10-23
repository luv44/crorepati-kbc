import { expect, test } from '@playwright/test';

async function onboard(page: import('@playwright/test').Page, exam = 'general-knowledge') {
  await page.goto('/');
  await page.getByLabel('Exam').selectOption(exam);
  await page.getByRole('button', { name: /Continue as guest/i }).click();
  await expect(page.getByRole('heading', { name: /A little wiser/i })).toBeVisible();
}

test('Current Live has independent date selectors, dated sources and honest empty state', async ({ page }) => {
  await onboard(page);
  await page.goto('/current-affairs');
  await expect(page.getByRole('heading', { name: 'Current Live' })).toBeVisible();
  await expect(page.getByLabel('News year')).toHaveValue('2026');
  await expect(page.getByLabel('News month')).toHaveValue('10');
  await expect(page.getByLabel('News day')).toHaveValue('22');
  await expect(page.getByText('International Relations', { exact: true })).toBeVisible();
  const source = page.getByRole('link', { name: /Official PIB India–Poland joint statement/i });
  await expect(source).toHaveAttribute('target', '_blank');
  await expect(source).toHaveAttribute('rel', 'noopener noreferrer');
  await page.getByLabel('News day').selectOption('10');
  await expect(page.getByRole('heading', { name: 'No verified news found' })).toBeVisible();
});

test('new exam dropdown scopes Learn and Practice to the same mapping', async ({ page }) => {
  await onboard(page, 'ctet');
  await page.goto('/learn');
  await expect(page.getByRole('heading', { name: 'CTET' })).toBeVisible();
  await expect(page.locator('.subject-card')).toHaveCount(14);
  await page.goto('/practice');
  const subject = page.getByLabel('Subject');
  await expect(subject.locator('option')).toHaveCount(15);
  await page.locator('.exam-selector.compact select').selectOption('ibps-po');
  await expect(subject.locator('option')).toHaveCount(13);
});

test('every answered question exposes a forward control and unanswered questions can be skipped', async ({ page }) => {
  await onboard(page);
  await page.goto('/practice?count=5');
  await page.getByRole('button', { name: 'Start session' }).click();
  await expect(page.getByRole('button', { name: 'Skip this one' })).toBeVisible();
  await page.locator('.answer-option').first().click();
  await expect(page.getByRole('button', { name: 'Next question' })).toBeVisible();
});
