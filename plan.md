小紅書 Content Generator - Phased Development Plan

## Overview

This is an AI-powered 小红书 (Xiaohongshu/RedNote) content generator designed to help build a professional personal brand. The system transforms technical content from various sources into engaging social media posts optimized for the Chinese professional networking platform.

---

## Phase 1: Foundation & Text Input (Week 1)

**Goal**: Get basic content generation working with text input

### Tasks (10 hours)

#### Setup (2 hours)

- [x] Initialize project structure
- [x] Set up Claude API or MCP connection (Using OpenAI API + MCP with FastMCP)
- [x] Create basic CLI interface (MCP server for Claude Desktop)

#### Core Generator (5 hours)

- [x] Build prompt template for 小紅書 style (GENERATOR_PROMPT & CRITIC_PROMPT)
- [x] Implement text-to-post conversion (Multi-agent workflow: generator → critic → improve)
- [x] Add emoji and hashtag generation (Built into prompts)
- [x] Test with 5-10 sample topics (Tested with RAG topic)

#### Output Formatting (3 hours)

- [x] Structure posts (hook, body, CTA) (Handled by prompts)
- [x] Add character count optimization
- [ ] Create 3 template variations

**Deliverable**: ✓ CLI tool that takes text input and generates 小紅書 posts

---

## Phase 2: Audience Targeting & Tone (Week 4)

**Goal**: Optimize for different professional audiences

### Tasks (10 hours)

#### Audience Profiles (3 hours)

- [ ] Create CTOs/Engineering Directors profile
- [ ] Create Hiring Managers profile
- [ ] Create Software Engineers profile
- [ ] Create Business Leaders profile

#### Tone Adaptation (4 hours)

- [ ] Adjust technical depth per audience
- [ ] Emphasize different value props
- [ ] A/B test different approaches
- [ ] Create tone guidelines document

#### Template Library (3 hours)

- [ ] Build template: Problem → Solution → Impact
- [ ] Build template: Insight → Application → CTA
- [ ] Build template: Story → Learning → Takeaway
- [ ] Create 2-5 additional template variations
- [ ] Test all templates with different audiences

**Deliverable**: ✓ Audience-aware content generation

---

## Phase 3: Quality & Polish (Week 5)

**Goal**: Improve output quality and user experience

### Tasks (10 hours)

#### Output Enhancement (4 hours)

- [ ] Better hashtag selection
- [ ] Emoji placement optimization
- [ ] Hook strength improvement
- [ ] CTA variations

#### Batch Processing (3 hours)

- [ ] Process multiple inputs at once
- [ ] Queue system for content ideas
- [ ] Save drafts for review

#### UI Improvements (3 hours)

- [ ] Better CLI prompts
- [ ] Progress indicators
- [ ] Preview before saving
- [ ] Simple config file

**Deliverable**: ✓ Production-ready generator with good UX

---

## Phase 4: URL Processing (Week 2)

**Goal**: Extract and process web content

### Tasks (10 hours)

#### Web Fetching (4 hours)

- [ ] Implement URL content extraction (Skeleton in web.py, needs implementation)
- [ ] Handle common article formats
- [ ] Extract title, main content, key points
- [ ] Error handling for failed fetches

#### Content Summarization (4 hours)

- [ ] Identify key technical insights
- [ ] Extract business value points
- [ ] Filter noise/ads/navigation
- [ ] Test with 10 different URLs

#### Integration (2 hours)

- [ ] Combine URL processing with generator
- [ ] Add URL validation
- [ ] Test end-to-end workflow

**Deliverable**: ✓ System processes both text and URLs

---

## Phase 5: File Upload Support (Week 3)

**Goal**: Handle document inputs

### Tasks (10 hours)

#### Document Parsing (5 hours)

- [ ] PDF text extraction (Skeleton in extract.py, needs implementation)
- [ ] Markdown parsing
- [ ] TXT file handling
- [ ] Basic DOCX support (if time permits)

#### Content Processing (3 hours)

- [ ] Chunk long documents
- [ ] Extract headings/structure
- [ ] Identify key sections
- [ ] Handle code snippets

#### Testing & Refinement (2 hours)

- [ ] Test with various document types
- [ ] Improve extraction quality
- [ ] Add file size limits

**Deliverable**: ✓ Full multi-format input support (text, URL, files)

---

## Phase 6: Analytics & Iteration (Week 6)

**Goal**: Track performance and refine

### Tasks (10 hours)

#### Simple Analytics (3 hours)

- [ ] Track posts generated
- [ ] Log successful patterns
- [ ] Store best-performing templates
- [ ] Create performance metrics

#### Content Calendar (3 hours)

- [ ] Weekly posting schedule
- [ ] Topic categorization
- [ ] Variety tracking (avoid repetition)
- [ ] Export to CSV/calendar format

#### Documentation & Deployment (4 hours)

- [ ] Write usage guide
- [ ] Create example workflows
- [ ] Package for easy setup
- [ ] Document best practices learned

**Deliverable**: ✓ Complete system with analytics and documentation

---

## Daily 2-Hour Schedule

### Weekdays (Mon-Fri)

- [ ] **First 30 min**: Planning & review
- [ ] **Next 60 min**: Core development
- [ ] **Last 30 min**: Testing & documentation

### Weekends

- [ ] Use for catch-up or getting ahead
- [ ] Testing with real content
- [ ] Creating your own posts

---

## Success Metrics by Phase

| Phase | Key Metric                             |
| ----- | -------------------------------------- |
| 1     | Generate 10 quality posts from text    |
| 2     | Process 20 different URLs successfully |
| 3     | Handle 5+ document types               |
| 4     | 4 distinct audience variations         |
| 5     | <30 seconds per post generation        |
| 6     | Content calendar with 30 days planned  |

---

## Flexibility Buffer

Each phase has ~1-2 hours of buffer.

### If you finish early:

- [ ] Move to next phase
- [ ] Refine current features
- [ ] Create more templates
- [ ] Test with real content

### If you fall behind:

- [ ] Cut optional features
- [ ] Simplify implementation
- [ ] Focus on core value

---

## After 6 Weeks

You'll have a working system to:

- [ ] Generate posts from any input format
- [ ] Target different professional audiences
- [ ] Maintain consistent posting schedule
- [ ] Track what works
- [ ] Build your personal brand

**Next steps**:

- [ ] Start posting daily
- [ ] Gather feedback
- [ ] Iterate based on engagement data
