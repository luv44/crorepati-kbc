import { expect, test } from '@playwright/test';

async function onboard(page: import('@playwright/test').Page, exam = 'general-knowledge') {
  await page.goto('/');
  await page.getByLabel('Exam').selectOption(exam);
  await expect(page.locator('.interest-grid')).toHaveCount(0);
  await expect(page.getByText('S01 India Basics', { exact: true })).toHaveCount(0);
  await page.getByRole('button', { name: /Continue as guest/i }).click();
  await expect(page.getByRole('heading', { name: /A little wiser/i })).toBeVisible();
  await expect(page.getByRole('link', { name: /Read verified Current Live/i })).toBeVisible();
}

test('Current Live exposes every same-date story and each story-linked quiz without a display cap', async ({ page }) => {
  await onboard(page);
  await page.goto('/current-affairs');
  await expect(page.getByRole('heading', { name: 'Current Live' })).toBeVisible();
  await expect(page.getByLabel('News year')).toHaveValue('2026');
  await expect(page.getByLabel('News month')).toHaveValue('10');
  await expect(page.getByLabel('News day')).toHaveValue('23');
  await expect(page.getByRole('tab', { name: /1-minute brief/i })).toHaveAttribute('aria-selected', 'true');
  await expect(page.getByText(/Showing all 10 independently verified stories.*no story limit/i)).toBeVisible();
  const storyNavigation = page.getByRole('navigation', { name: 'All stories for selected date' });
  await expect(storyNavigation.getByRole('button')).toHaveCount(10);
  await expect(storyNavigation.getByText('Defence', { exact: true }).first()).toBeVisible();
  await expect(page.getByText('KEY POINTS', { exact: true })).toBeVisible();
  await expect(page.getByText('WHAT TO REMEMBER', { exact: true })).toBeVisible();
  await expect(page.getByText('QUESTIONS FOR THIS STORY', { exact: true })).toBeVisible();
  await expect(page.locator('.story-question-preview ol > li')).toHaveCount(2);
  await expect(page.locator('.story-question-preview .preview-options > span')).toHaveCount(8);
  await expect(page.getByText(/Cached with the app for offline reading/i)).toBeVisible();
  await expect(page.getByLabel('Verified current news run target')).toContainText('13 / 150 checked records');
  await expect(page.getByLabel('Current news topic')).toHaveValue('all');
  await page.getByLabel('Current news topic').selectOption('Economy');
  await expect(page.getByRole('navigation', { name: 'All stories for selected date' }).getByRole('button')).toHaveCount(1);
  await page.getByLabel('Current news topic').selectOption('all');
  await page.getByRole('navigation', { name: 'All stories for selected date' }).getByRole('button').first().click();

  await page.getByRole('button', { name: 'Save brief' }).click();
  await expect(page.getByRole('button', { name: 'Saved', exact: true })).toBeVisible();
  await expect(page.getByLabel('Saved current affairs briefs')).toContainText('Defence');
  const source = page.getByRole('link', { name: /PIB — Ministry of Defence release/i });
  await expect(source).toHaveAttribute('target', '_blank');
  await expect(source).toHaveAttribute('rel', 'noopener noreferrer');

  await page.getByRole('button', { name: /Answer this story's 2 questions/i }).click();
  await expect(page.getByText('STORY QUESTIONS', { exact: true })).toBeVisible();
  await expect(page.locator('.daily-news-quiz .news-options button')).toHaveCount(4);
  await page.locator('.daily-news-quiz .news-options button').first().click();
  await page.getByRole('button', { name: 'Next question' }).click();
  await page.getByRole('button', { name: 'Skip & see result' }).click();
  await expect(page.getByText('STORY QUIZ COMPLETE', { exact: true })).toBeVisible();

  await page.getByRole('button', { name: /Review the briefs/i }).click();
  await page.getByRole('tab', { name: /All questions 20/i }).click();
  await expect(page.locator('.daily-quiz-header > strong')).toHaveText('1 / 20');

  await page.getByLabel('News day').selectOption('10');
  await expect(page.getByRole('heading', { name: 'No verified news found' })).toBeVisible();
});

test('new exam dropdown scopes Learn and Practice to the same mapping', async ({ page }) => {
  await onboard(page, 'ctet');
  await page.goto('/learn');
  await expect(page.getByRole('heading', { level: 1, name: 'CTET' })).toBeVisible();
  await expect(page.locator('.subject-card')).toHaveCount(14);
  await page.goto('/practice');
  const subject = page.getByLabel('Subject');
  await expect(subject.locator('option')).toHaveCount(15);
  await page.locator('.exam-selector.compact select').selectOption('ibps-po');
  await expect(subject.locator('option')).toHaveCount(13);
  await page.locator('.exam-selector.compact select').selectOption('kbc-crorepati');
  await expect(subject.locator('option')).toHaveCount(27);
  await page.goto('/learn');
  await expect(page.getByRole('heading', { level: 1, name: 'KBC Crorepati' })).toBeVisible();
  await expect(page.locator('.subject-card')).toHaveCount(26);
});

test('practice discards an invalid draft, opens selected questions and keeps forward controls visible', async ({ page }) => {
  await onboard(page);
  const fixture = await page.evaluate(async () => {
    const starter = await (await fetch('/data/starter.json')).json();
    return { questionId: starter.questions[0].id as string, legacyTopicId: starter.factCards.find((fact: { evidence: unknown }) => !Array.isArray(fact.evidence)).topicId as string };
  });
  await page.evaluate(id => sessionStorage.setItem('cr-session-practice:count=5:exam=general-knowledge', JSON.stringify({ id: 'stale-draft', examId: 'general-knowledge', ids: [id], index: 1, answers: {}, started: Date.now(), deadline: null, mode: 'practice', negative: 0, finished: false, hintUsed: false, eliminateUsed: false, eliminated: [], hintFor: null })), fixture.questionId);
  await page.goto('/practice?count=5');
  await page.getByRole('button', { name: /Start 5-question session/i }).click();
  await expect(page.getByRole('button', { name: 'Skip this one' })).toBeVisible();
  const examSelector = page.locator('.exam-selector.compact select');
  await examSelector.selectOption('ibps-po');
  await expect(page.getByRole('button', { name: /Start 5-question session/i })).toBeVisible();
  expect(await page.evaluate(() => sessionStorage.getItem('cr-session-practice:count=5:exam=ibps-po'))).toBeNull();
  await examSelector.selectOption('general-knowledge');
  await expect(page.getByRole('button', { name: 'Skip this one' })).toBeVisible();
  const focusedStem = await page.locator('.question-title').innerText();
  expect(focusedStem).not.toMatch(/advanced exam perspective|syllabus|curriculum|benchmarks|evaluat|scrutiny/i);
  const focusedOptions = await page.locator('.answer-option > span:nth-child(2)').allInnerTexts();
  expect(focusedOptions).toHaveLength(4);
  expect(Math.max(...focusedOptions.map(option => option.length))).toBeLessThanOrEqual(160);
  await page.locator('.answer-option').first().click();
  await expect(page.getByRole('button', { name: 'Next question' })).toBeVisible();
  await page.goto(`/topic/${fixture.legacyTopicId}`);
  await page.getByText('View evidence & source').click();
  await expect(page.getByText(/does not yet have a structured direct-source excerpt/i)).toBeVisible();
});
