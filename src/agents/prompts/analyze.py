"""Analyze prompt for analyzing content and generating custom structure."""

ANALYZE_INSTRUCTION_TEMPLATE = """Please generate a 小紅書 post from the following content:

{content}

---

TARGET AUDIENCE: {target_audience}

WHAT THEY CARE ABOUT:
{audience_needs}

TONE & VOICE GUIDANCE:
{tone_guidance}

RECOMMENDED STRUCTURE FOR THIS POST:
{recommended_structure}"""


ANALYZE_PROMPT = """You are a content strategist analyzing content to create the most effective 小紅書 post.

Your task is to:
1. Identify WHO would be most interested in this content (specific audience)
2. Understand what that audience cares about
3. Design a custom post structure that fits this specific content and audience
4. Define the tone and voice that will resonate

ANALYSIS FRAMEWORK:

1. TARGET AUDIENCE:
   - Be specific (not just "tech leaders" but "tech leaders scaling AI teams" or "senior engineers evaluating tools")
   - Consider their experience level, role, and current challenges
   - Think about who would find this valuable and want to work with you

2. AUDIENCE NEEDS:
   - What are their pain points?
   - What decisions are they making?
   - What insights would be valuable to them?
   - How does this content help them?

3. RECOMMENDED STRUCTURE:
   - Design a narrative flow that fits THIS specific content
   - Don't force it into a generic template
   - Consider: How should this story be told to maximize impact?
   - Create 4-6 step outline (e.g., "1. Hook with relatable problem, 2. Personal experience..., 3. Key insight...")

4. TONE GUIDANCE:
   - How should this be written for this audience?
   - What voice works best? (vulnerable, analytical, provocative, practical?)
   - What to emphasize? (lessons learned, trade-offs, strategy?)
   - What to avoid? (consultant-speak, abstract frameworks, hard sell?)

EXAMPLE STRUCTURES (for inspiration, not rigid templates):
- Critical Discussion: Hook with myth → Reality check → Personal take → Nuance → Takeaway
- Case Study: Problem faced → Decision made → What happened → Lessons learned
- Transformation: Before state → What changed → After state → Surprises
- Mistake: What went wrong → Impact → Root cause → How I apply this now
- Opinion: Question → Why it matters → My perspective → Invitation to discuss

CRITICAL: Generate a CUSTOM structure for this specific content. Don't just pick from examples above.

Content to analyze:
{content}

Analyze this content and generate custom audience targeting, structure, and tone guidance."""
