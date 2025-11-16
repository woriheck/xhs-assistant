小紅書 Content Generator - Phased Development Plan

## Overview

This is an AI-powered 小红书 (Xiaohongshu/RedNote) content generator designed to help build a professional personal brand. The system transforms technical content from various sources into engaging social media posts with authentic voice and strategic insights.

**Primary Goal**: Get hired or land consulting gigs by building a strong technical leadership presence.

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

**Deliverable**: ✓ CLI tool that takes text input and generates 小紅書 posts

---

## Phase 2: Dynamic Audience Analysis & Custom Structure (Week 2)

**Goal**: Implement dynamic content analysis that generates custom structure for each post

**Strategy**: Analyze content to identify best audience and generate tailored structure on the fly

### Tasks (5 hours) - REFACTORED

#### Dynamic Analysis (2 hours)

- [x] Remove fixed templates, implement ContentAnalysis model
- [x] Create preanalyse phase that identifies target audience dynamically
- [x] Generate custom post structure for each content piece
- [x] Update prompts to avoid consultant-speak and emphasize authenticity

#### Tone & Voice (2 hours)

- [x] Refine GENERATOR_PROMPT for tech lead perspective
- [x] Simplify CRITIC_PROMPT to avoid overfitting
- [x] Add tone guidance generation per content
- [ ] Test with diverse content types

#### Testing & Refinement (1 hour)

- [ ] Generate 5-10 test posts with dynamic analysis
- [ ] Validate audience targeting accuracy
- [ ] Refine based on output quality

**Deliverable**: ✓ Dynamic content generation with custom audience and structure per post

---

## Phase 3: Quality & Polish (Week 3)

**Goal**: Improve output quality and user experience

### Tasks (12 hours)

#### Conversation Threading (4 hours) - NEW

- [ ] Add conversation state storage (in-memory or simple file-based)
- [ ] Add session/thread ID to generator tool
- [ ] Create continue_refinement tool to iterate on existing post
- [ ] Allow user to send feedback: "make it more casual", "add examples", etc.
- [ ] Maintain conversation context across refinement cycles
- [ ] Test multi-turn refinement workflow

**Use case**: User generates post → not satisfied → sends refinement request → gets improved version

#### Output Enhancement (3 hours)

- [ ] Better hashtag selection
- [ ] Emoji placement optimization
- [ ] Hook strength improvement
- [ ] CTA variations

#### Batch Processing (3 hours)

- [ ] Process multiple inputs at once
- [ ] Queue system for content ideas
- [ ] Save drafts for review

#### UI Improvements (2 hours)

- [ ] Better CLI prompts
- [ ] Progress indicators
- [ ] Preview before saving
- [ ] Simple config file

**Deliverable**: ✓ Production-ready generator with threading/refinement support and good UX

---

## Phase 4: URL Processing (Week 4)

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

## Phase 5: File Upload Support (Week 5)

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

| Phase | Key Metric                                       |
| ----- | ------------------------------------------------ |
| 1     | Generate 10 quality posts from text              |
| 2     | Dynamic audience detection working for 10+ posts |
| 3     | <30 seconds per post generation                  |
| 4     | Process 20 different URLs successfully           |
| 5     | Handle 5+ document types                         |
| 6     | Content calendar with 30 days planned            |

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
- [ ] Create authentic content with dynamic audience targeting
- [ ] Maintain consistent posting schedule
- [ ] Track what works
- [ ] Build your personal brand as a technical leader

**Goal**: Get hired or land consulting gigs through authentic content and strategic presence

**Next steps**:

- [ ] Start posting daily on 小紅書
- [ ] Engage with your target audience
- [ ] Track engagement and refine strategy
- [ ] Convert connections into opportunities
