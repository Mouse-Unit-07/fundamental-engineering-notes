# How to Manage

- How to manage notes
- ...management is closely tied to the way engineering should be conducted- refer to technical essentials and DevOps notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Accountability](#accountability)
- [Agile vs Project Management](#agile-vs-project-management)
- [Alpha Geek](#alpha-geek)
- [Architecture Review](#architecture-review)
- [BS Umbrella](#bs-umbrella)
- [Calibrate Your Response](#calibrate-your-response)
- [Career Growth](#career-growth)
- [Coaching](#coaching)
- [Code Reviews](#code-reviews)
- [Communicate Effectively](#communicate-effectively)
- [Communication/Leadership Gaps](#communicationleadership-gaps)
- [Delivering Bad News](#delivering-bad-news)
- [Detach](#detach)
- [Discrimination](#discrimination)
- [Don't Monopolize Interesting Work](#dont-monopolize-interesting-work)
- [Don't Stop Learning](#dont-stop-learning)
- [Exposure to Others](#exposure-to-others)
- [Feedback](#feedback)
- [How to Manage a Project](#how-to-manage-a-project)
- [Lead Technical Decisions](#lead-technical-decisions)
- [Listen](#listen)
- [Make a Decision](#make-a-decision)
- [Management Categories](#management-categories)
- [Mentoring](#mentoring)
- [Micromanager](#micromanager)
- [Onboarding Documents](#onboarding-documents)
- [One-On-One Meetings](#one-on-one-meetings)
- [Outage Postmortem](#outage-postmortem)
- [Overriding Technical Decisions](#overriding-technical-decisions)
- [People Pleaser](#people-pleaser)
- [Preparing a Project](#preparing-a-project)
- [Process Czar](#process-czar)
- [Promotion](#promotion)
- [Questions To Ask a Mentee](#questions-to-ask-a-mentee)
- [Review Decision and Process Outcomes](#review-decision-and-process-outcomes)
- [Set Expectations](#set-expectations)
- [Standards for Code and Systems](#standards-for-code-and-systems)
- [Stay Out of Management Role As Needed](#stay-out-of-management-role-as-needed)
- [Stay Technically Relevant](#stay-technically-relevant)
- [The Larger Picture](#the-larger-picture)
- [True North](#true-north)
- [Understand the Architecture](#understand-the-architecture)
- [Virtues of Laziness/Impatience](#virtues-of-lazinessimpatience)
- [Warning Signs](#warning-signs)

## Overview

- > ... there is nothing more difficult to carry out, nor more doubtful of success, nor more dangerous to handle, than to initiate a new order of things. For the reformer makes enemies of all those who profit by the old order, and only lukewarm defenders in all those who would profit by the new order...
  - Niccolo Machiavelli in "The Prince" section vi
- > New engineering managers think of the job as a promotion, giving them seniority on engineering tasks and questions. This is a great approach for ensuring they remain junior managers, and unsuccessful leaders at that. It’s hard to accept that “new manager” is an entry-level job with no seniority on any front, but that’s the best mindset with which to start leading
  - Marc Hedlund in _The Manager's Path_
- > If your team needs a manager more than they need an engineer, you have to accept that being that manager means that you by definition can’t be that engineer. I know some people manage both, but you need to decide, if you’re going to suck at one, which one that will be. I feel bad when I suck at being an engineer, but sucking at being a manager would be a choice I inflicted on other people. That’s not fair.
  - Cate Custon in _The Manager's Path_
- > One thing that managers have to keep in mind is that part of their job is to ferret out problems proactively. There exists an idea that if you make yourself accessible, hold office hours where anyone can meet with you, and tell the team that you are always available, people will naturally bring their problems to your office. There’s no need to seek them out, because your team trusts you enough to come to you when things are going wrong. Except this basically never happens. The open-door policy is nice in theory, but it takes an extremely brave engineer to willingly take the risk of going to her boss (or especially her boss’s boss, etc.) to tell him about problems. That even assumes that the engineer knows what the problems actually are well enough to explain them! Even on teams you build yourself, where there’s a huge level of trust and respect, some problems will just never get escalated to you. Some of these problems will cause people to leave, projects to get delayed, failures to explode. You turn your back, and the next minute a team that seemed fine has crumbled.
  - Camille Fournier in _The Manager's Path_
- Good leaders write well, read carefully, listen carefully, can get up in front of a group and speak, pay attention in meetings, and are constantly testing the limits of both their own and the team's knowledge

## Accountability

- The role of managers is to take accountability for the health and productivity of teams. That means they're accountable for:
- Unstable product road maps
  - Unproductive teams, unstable systems, goals are constantly changing, and everything is always urgent
- Errant tech lead
  - Tech lead is down the rabbit hole redesigning some core system
  - Design doc is barely started, work is piling up, but tech lead insists that the problem can't be rushed
- Full-time firefighting mode
  - Manager inherited a bunch of legacy systems that are constantly broken, and teams are always fighting fires
  - There's a roadmap being worked on to get the legacy systems out, but there aren't any updates on the roadmap's status
- ...if the organization as a whole is constantly changing goals, the manger should identify the changes that are causing problems and work w/ product to explain the problem and refocus on what's important

## Agile vs Project Management

- Agile software development doesn't get rid of project management as a role
- Agile just emphasizes breaking down tasks into smaller pieces for iterative development and frequent releases
- Project management isn't always needed as opposed to Agile
  - It's a waste of time if project managers are acting as crutches for engineers
  - ...but if engineers aren't working effectively/efficiently together, then project management is needed
- Value of project management
  - There's value in the enforcement of self-discipline to think about projects in some depth before diving in and seeing what happens
  - It's not in being able to predict the future, catch every detail beforehand, etc (all not possible)
  - The resulting plan (however effective) is less important than taking the time to plan

## Alpha Geek

- Sometimes there are self-centered, intolerable, but knowledgeable engineers ("alpha geeks")
- Characteristics include:
  - Wanting to be the best engineer on the team
  - Always has the right answer
  - Solves all the hard problems
  - Values intelligence and technical skill above all traits, and believes that's what should determine who makes decisions
  - Can't deal w/ dissent, and easily threatened by those perceived as trying to steal their spotlight, or capable of upstaging them
  - Responds only to messages that support them to be the best
  - Builds a culture of fear in an attempt to create a culture of excellence
  - Undermines the people that work for them by belittling their mistakes, worst case redoing their work without warning
  - Takes all the credit of work instead of acknowledging the strengths of team members
  - Can't let anyone else get any glory without claiming some of it for themselves
  - Convinced their always a part of good ideas, and never a part of bad ideas unless they know the ideas'll fail
  - Will point out your ignorance if you don't know something
  - Rigid about how things should be done, and closed off to new ideas they didn't come up with
  - Feel threatened in response to complaints about systems they built, or their past technical decisions
  - Demeaning towards those that don't have technical roles, and hate listening to those they don't respect intellectually
  - Hide information from others to maintain their edge
- If you're skilled but people never come to you w/ questions, compare yourself to above list and reflect
- Aggressive habits make horrible managers
- We need to let go of the facade that we're the best (it's never true)
- Don't promote alpha geeks
  - They're harmful to collaboration, and undermine those that feel unable to fight back

## Architecture Review

- When reviewing a system's architecture, the objective is to highlight any new changes and associated risks
- Questions to ask:
  - How many people on the team are comfortable using this new system/writing this new language?
  - Do we have production standards in place for this new thing?
  - What is the process for rolling this out and training people to use it?
  - Are there new operational considerations for using this?
- Be specific about the changes that need review
  - Could be new languages, frameworks, storage systems, developer tooling, etc
  - ...we all want to modify the architecture to prevent teams from designing new features poorly, but it's unrealistic for both small and large companies
    - In other words, it's easier to suggest overhauling changes for static parts first
- Suggest everyone to prepare for the review
  - By giving people time to think about the proposed change, it forces them to find risks in the change and why/whether the change is needed
- Choose the review board wisely
  - Include the people that are most affected by the change, and not just a static group of gurus
  - Avoid inviting people that aren't relevant, and pull in those that are relevant to be a part of making the architecture change decision

## BS Umbrella

- Shielding your team from distractions is helpful
  - ...or rather, helping the team understand key important goals and having them focus on the goals is important
- Unfortunately, it's unrealistic to think you can shield your team from everything
- Whether it's sales, layoffs, etc, letting some stress through to the team is sometimes important
  - Company-wide stress puts their work in context, and can get engineers to focus
  - We all need to know why we're working on what we're working on
- Don't deny any drama that's actually happening
  - In other words, don't bet on your employees being idiots
  - Neutralize gossip by addressing the drama in a low-emotion way
- Don't be a parent
  - Your employees are independent adults

## Calibrate Your Response

- Adjust to a mentee's responses
  - You need to adjust according to a mentee's successes and failures
- If they're competent, you might get away w/ checking in w/ them less than once a week, but check in once a week anyway

## Career Growth

- Your manager isn't obligated to direct you to any career growth, but is nonetheless the liaison between you and the bureaucracy of the company
  - There's some responsibility to help find training, whether it's a conference to attend, a class to take, a book to read, or talking to someone in the company
- Training available for employees vary by company
  - You're responsible for bringing up what kind of training you want

## Coaching

- Refers to a structured conversational approach for managers to help employees improve performance by:
  - Asking guided questions
  - Helping employees reflect
  - Helping employees find their own solutions
  - Encouraging experimentation and growth
  - Providing support and accountability
- Different from raw management, in that it removes micromanagement aspects

## Code Reviews

- Code review is a modern standard
- They're needed for ensuring codebase stability and quality, but they should be straight forward and efficient:
  - Make expectations clear
    - Code reviews don't catch bugs (you can talk about how likely bugs are, but regardless of the extent you're still speculating)
    - Tests catch bugs
    - Code reviews should be a socializing exercise to catch people up on changes
  - Use a linter
    - Talking about style, formatting, etc is a waste of time
    - Run code through a linter before starting a code review
    - Nitpicking/criticism on style/formatting is unproductive at best, and is bullying at worst
  - Have a review backlog and check it
    - As in, limit the number of code review requests that a person can be assigned

## Communicate Effectively

- > Years ago, I was fortunate to receive a PhD in mathematics from one of the most prestigious Applied Mathematics programs in the Unites States. One of the judges on my panel was a renowned mathematician in the field of numerical analysis. Something he said to me after my (successful) defense has stuck with me throughout my working career (not in mathematics!). He said, “Your thesis was one of the most lucid and clear theses I’ve read in many years. Thank you!” I was certainly gratified but also very surprised by his words. I had assumed that he, being a world-class mathematician, would “know all about it,” and just “watch” how my thesis would turn out. In fact, as he explained, he was able to do that, but only because I had taken the trouble to explain the basic ideas of the problem space and the motivations behind my ideas. I have never forgotten this lesson. Since then, after many years working in software and in large organizations, I have come to appreciate those comments even more.
  - Michael Marçal in _The Manager's Path_
- First listen and observe to understand where your mentee stands
- Then try to communicate in a way that the mentee understands
- Senior engineers often have a bad habit of lecturing and debating w/ anyone that disagrees w/ them or doesn't understand them- don't do that

## Communication/Leadership Gaps

- Don't become a "process czar" in an attempt to solve communication and leadership issues
- Forcing people to follow a process helps, but it's not a silver bullet
- Employ self-regulating processes
  - Processes should be clear and easy to follow, and should minimize need for a leader to play a cop role to make sure people are obliging

## Delivering Bad News

- Whether it's layoffs or a team being broken down, there are do's and don't do's:
- Don't:
  - Blast an impersonal message to a large group
    - Aka, email/chat
    - Don't blast a message to a room filled w/ people either
    - Individuals have the right to hear bad news from a manager directly
    - Hearing news directly helps guide away from misunderstanding and animosity too
  - Force yourself to deliver a message you can't stand behind
    - Have someone else deliver the news if you strongly disagree w/ what you need to tell
- Do:
  - Talk to individuals as much as possible
    - Tailor messages to those you expect to react the most
    - Emphasize that the orders are marching orders that you have to be on board w/
  - Be honest about likely outcomes
    - Talk about the perspectives from which the decisions were made
  - Think about how you'd like to be told
    - Treat people like you'd like to be treated

## Detach

- As in, depersonalize yourself from your decisions and what you do/say
- If you don't detach:
  - You'll be accused of playing favorites
  - People won't take your words seriously
  - You'll be tempted to talk about high-level/impactful decisions that can be harmful
- ...but don't go too far as to treat people like cogs
- > As you grow more detached from the team, it can be easy to start to dehumanize people and treat them like cogs. People can tell when that’s happening, when their leaders stop caring about the individuals in the organization. They’re less likely to feel committed to giving their all, to taking risks and pushing through hard circumstances, if they feel that no one really cares about them personally. Nurturing that kind of connection, even at a superficial-seeming level, helps to reinforce that you do care about them and not just their current projects or work output; that you know they’re people outside of work. It grounds you without attaching you too strongly to individuals. You’ll have to make hard calls as an executive, but your team deserves a leader who’s able to be kind even while making those hard calls.
  - Camille Fournier in _The Manager's Path_

## Discrimination

- Along w/ harassment, microaggression, etc that you (hopefully) read about in an HR document, pairing mentees w/ mentors based on non-technical reasons is also discrimination
- Pairing only men w/ men, women w/ women, people of color w/ people of color, etc
- Engineers should be paired based on their roles and whether their skill sets have synergy

## Don't Monopolize Interesting Work

- Senior engineers in the position of management shouldn't be doing neither the most interesting work or boring work all the time
- Doing tricky/boring/annoying areas of work emphasizes where processes are broken
- As a senior engineer, it also makes sense to be delegated harder work

## Don't Stop Learning

- Over the years you encounter "best practices" and scars caused by mistakes
- Technology is always changing, so we need to continually experience that change
- As you mentor someone and explain how things are, you'll see patterns in the way things are done (may be good or bad)
  - Creativity is both about seeing new things and seeing patterns hidden in others
  - Working w/ those w/ fresh perspectives helps see new patterns

## Exposure to Others

- Introduce mentees to others in the company
- Human networks are great for transmitting knowledge/information quickly
- Don't abuse mentees- the tech world is small

## Feedback

- A manager needs to provide feedback
  - This doesn't mean performance reviews (although that's a part of it)
  - This means a talk about any screw-ups, and ways to improve
- Feedback talks can be uncomfortable, but the only thing worse than getting behavioral feedback is not getting any at all (or feedback just during performance reviews)
- The faster you get feedback about bad habits, the faster you can fix them
- A good manager will note both the good and bad habits you have, and inform you about both, and prioritize the need to inform employees over finding the right time to provide feedback
- Publicity
  - Positive feedback can be public to reinforce the behavior across a team
  - Negative feedback should be private to avoid spreading fear of making mistakes
- As you become senior:
  - Feedback decreases
  - Changes from personal to team/strategy-related input
- A manager should also proactively ask for feedback from mentees
  - Not that new engineers should attack existing teams/processes, but that a new perspective on a system you've been working on is precious
- Common feedback items
  - Struggling to say no to distractions and helping others instead of finishing their own work
  - Good work, but hard for others to work w/, overly critical/rude in meetings, code reviews, or other collaborative activities
  - Lack of breaking work into smaller deliverables, and not balancing planning and design w/ getting things done
  - Lack of following best practices accepted by the team, cutting corners, and other sloppy work
- A lack of feedback indicates that someone is ready for a promotion
  - Otherwise, there should be feedback guiding an employee to acquire missing skills
- Provide the receiver of feedback w/ time to prepare
  - Don't surprise those receiving feedback w/ sudden criticism
  - If there's a written document, give it to them before talking about it in a formal meeting
- Score sheets
  - Sheets grading an employee w/ numbers is uncomfortable to talk about when there's anything less than perfect
  - Make sure to explain how an employee can improve on each account
- **Continuous feedback**
  - Know your people
    - What are their goals, strengths/weaknesses?
    - What level is everyone, and what can be improved to move each person up?
  - Observe your people
    - Continuous feedback forces everyone to pay attention and look for both areas of improvement and praise
  - Provide lightweight, regular feedback
    - Start w/ positive feedback- it's essential to show awareness of what's being done well for someone to accept what they're not doing well
  - Provide "coaching"
    - Not essential for continuous feedback, but great when the two are paired together
- **Feedback template**
  - Account for more than the past couple of months if applicable
  - Use concrete examples, and excerpts from peers
    - Anonymous if needed
  - Spend time on accomplishments and strengths
    - Emphasizing what's good is important for raising employees to be competent for their next role
  - Keep areas of improvement focused

## How to Manage a Project

- Project management is:
  - Breaking a complex end goal down to smaller pieces
  - Putting the pieces in roughly the most effective order
  - Identifying the pieces that can be done in parallel, and which must be done in sequence
  - Attempting to squeeze out unknowns that'll cause the project to slow down or fail
  - Acknowledging that you'll miss some unknowns regardless of best efforts
- Guidelines
  - Break it down
    - Spreadsheet, Gantt chart, or whatever works
    - Ask questions if there are pieces that aren't clear
  - Push through all details and unknowns
    - The nitty gritty is usually irritating, boring, painful
    - Flush out all details and unknowns as much as possible, and only then move on
  - Run the project and adjust accordingly
    - W/ a clear outline of what's been done and what needs to be done, adjustments will be easier when things don't work
    - Use insights from project planning to handle requirements changes
  - Revisit details as you get close to completion
    - Go through all details to flush out what could fail
    - Look for missing items, tests, verifications, etc
    - Decide on what's "good enough" and commit to it
- Adjust management priorities according to project stages
  - At first, manager involvement is key to establishing clear goals and system design
  - Closer to delivery, progress details are less relevant- what's important is what specifics people are fighting
- Budget 20% for generic sustaining engineering work
  - This means testing, debugging, cleaning up legacy code, migrating language or platform versions, etc

## Lead Technical Decisions

- This means contribute to decision making- not that you should be making all the decisions alone
- Making decisions alone will lead to team members that resent you and blame you when things go wrong
- Making no decisions and leaving everything to the team slows down work without resolution
- What's important is identifying which decisions:
  - Can be made by you
  - Should be delegated to someone w/ more expertise
  - Require the whole team to resolve
- When technical decisions are on the table, clarify what's being discussed and inform everyone of the outcome

## Listen

> Listening is a precursor to empathy, which is one of the core skills of a quality manager. You need this skill wherever your career takes you: even principal engineers with no reports need to be able to hear what others are really saying. So when your mentee is speaking to you, pay attention to your own behavior. Are you spending all your time thinking about what you want to say next? Are you thinking about your own work? Are you doing anything other than listening to the words coming out of his mouth? If so, you're not listening well.
> (...)
> People are not good at saying precisely what they mean in aa way that others can exactly understand. We have yet to achieve Borg hive mind or Vulcan mind meld, so we're constantly pushing complex ideas through the eye of the needle of language. And language is not something that most engineers have mastered in nuance and interpretation. So listening goes beyond hearing the words your mentee is saying. When you're face to face with another person, you also have to interpret his body language and the way he's saying those words. Is he looking you in the eye? Is he smiling? Frowning? Sighing? These small signals give you a clue as to whether he feels understood or not.
>
> Camille Fournier in _The Manager's Path_

- If you're trying to convey something complicated or your mentee doesn't appear to understand, be prepared to reword what you said
  - Mentees are nervous of screwing up the opportunity, is trying their best to please you, and trying hard not to look stupid
  - Make sure to get as many questions of of a mentee as needed for clarification

## Make a Decision

- Just as in project management/planning, what's important is for leaders/managers to make decisions in a timely manner
  - There should be time integrated in the process to make informed/planned decisions, but also time to adjust after bad/inefficient decisions are made
- Pick a strategy and run w/ it- if it doesn't work, try something else
- It doesn't need to be perfect

## Management Categories

- Camille Fournier in _The Manager's Path_ cites _High Output Management_ by Andy Grove and his 4 management categories:
- **Information gathering/sharing**
  - Sitting in meetings, reading/writing emails, talking to people one on one, gathering perspectives
  - Managers need to synthesize information quickly, identify critical elements, and share information w/ appropriate parties in a comprehensive way
- **Nudging**
  - Reminding people of their commitments by asking questions instead of giving orders
  - Good for large teams where it's difficult to guide the team in the right direction
- **Decision making**
  - Taking conflicting perspectives and incomplete information and setting a direction (knowing that consequences of a poor decision will impact both you and the whole team)
  - The most draining and stressful parts of the job
- **Role modeling**
  - Showing people what the values of the company are
  - Showing up for commitments
  - Showing the best example for the team even when you don't feel like it

## Mentoring

- > Great talent is sometimes squandered by weak mentors who do little but ignore their charges, waste their time with trivial projects, or, worst of all, intimidate and belittle them out of ever wanting to join the organization. But you, dear reader, don't want to do this. You want to be a great mentor!
  - Camille Fournier in _The Manager's Path_
- If you don't want to mentor, then say so instead of saying yes and failing to deliver
- Worst case:
  - Mentee is a drain on the manager's time, and causes less work to be done
  - A mentor does such a horrible job that the mentee (that a company would otherwise want to keep) opts to leave early
    - This second case is much more common than the first
- Measurable goals
  - Set clear measurable goals to make improvement steps clear
- Clarify why you have a mentee
  - Either:
    - You're helping someone get up to speed
    - You're paired w/ a junior for career/skill growth
  - The second is often disappointing when both parties are busy driving on their own
- Mentoring is a responsibility
  - Mentoring takes time away from an engineer
  - Engineers working on time-sensitive tasks will suffer when they have to mentor at the same time
- Reward and train future leaders
  - For those that are impatient, practice empathy and humility
  - For introverts, go ahead and share your skills to develop stronger external perspectives

## Micromanager

- Don't keep your mentee on a leash and undermine them
- Instead, clarify what the goals and responsibilities are, and provide support/guidance as needed
- Sometimes, micromanagement is needed to have someone go in a precise/specific direction
- Trust your engineers after providing guidance
- Autonomy
  - Refers to control over some part of one's work
  - Micromanagers don't want to lose autonomy, and in exchange lose team members
- Don't abandon your team members
  - The opposite of micromanagement is completely ignoring a team member
  - Help them understand the responsibilities of the new role and provide support as needed
- Employ self-regulation
  - Point team members to measuring their own success, and make it visible to everyone
  - A team can be independent if they can safely regulate themselves to meet goals they're accountable for in some time period
- Gather information on your own before asking
  - It's annoying when micromanagers ask engineers when they could've found the information elsewhere (version control, etc)
  - Exposure of project status should be for both the team and managers

## Onboarding Documents

- Effective teams have good "onboarding documents" for new hires
- Onboarding documents include:
  - Step-by-step guides to set up development environments
  - Learning how tracking systems work
  - Familiarizing yourself w/ crucial tools needed for development
- Onboarding documents need to be maintained and updated to meet the changes of the workplace
- Having new hires update/modify the onboarding documents is a great way to kill two birds in one stone

## One-On-One Meetings

- The point of a 1-1 is to:
  - Create human connection between manager and employee
    - We're not robots- when things happen (death of a family member, new child, breakup, etc), we each need to be able to talk to each other about it
    - Being an introvert isn't an excuse to not make any connections- human connection is the bedrock of building trust and strong teams
    - True trust requires the ability and willingness to be vulnerable in front of each other
  - To speak privately about whatever needs discussing
    - 1-1s aren't to be driven completely by either party- both the manager and employee should be able to prepare a list of things to talk about
    - It's ok if 1-1s are reduced to once every weeks or whatever the frequency is, as long as they're not completely eliminated
    - 1-1s shouldn't be status meetings
      - If you're a manager reporting to a senior manager, then the 1-1 might be a technical status meeting for as long as there's nothing urgent that's non-technical to talk about
      - If you're an individual contributor reporting to a manager, then the 1-1 should be less technical and more human to avoid redundant talks- get the technical talk out of the way beforehand
- 1-1s should be weekly
  - This frequency avoids the need for manual rescheduling caused by infrequent 1-1s
  - Avoid times when either of you can potentially be out
- Mix it up
  - Go get lunch or coffee to talk
- Keep notes in a shared document for both of you to have
- Formats include:
  - Todo list
    - Both parties come in w/ a list of objectives to cover in order of importance
    - Updates given, decisions made/discussed, planning done
    - ...sometimes cold and made up of things that could've been handled w/ chat or email, but professional and efficient
  - Catch-up
    - The todo list format collapsed for less cold structure
    - Allows for more fluidity
    - ...must be careful to avoid turning into a complaining/therapy session
  - Feedback
    - If all there's to talk about is informal feedback and coaching, then that's ok too
    - If you're facing performance issues w/ a mentee/employee, these feedback 1-1s are crucial
    - Document both expectations you set w/ your mentee/employee, and the 1-1s you've had w/ them providing and receiving feedback
    - Don't wait to provide or receive feedback- same for praise
  - Progress report
    - This is for when you're managing managers
    - Progress reports from people you're working closely to is a waste of time

## Outage Postmortem

- After some failure, there needs to be a "learning review":
- Resist the urge to point fingers
  - Blaming people doesn't improve performance- it makes people afraid of making mistakes
- Understand the circumstances and context
  - By finding the factors that contributed to the failure, you can employ tests or tools for smoother incident management
- Be realistic about takeaways that are important
  - Pick just a handful of high-risk todo's amongst the monster todo list for improving the system, and let go off others for now

## Overriding Technical Decisions

- As a manager, you can reject someone's technical decision
- Be careful especially when you're a manager managing a manager
  - Those that are told to change their decisions will be sensitive when you're rewarded as a manager
  - Micromanaging's negative effects are dilated when you're a manager for managers
- When you're a manager, you have to let go of some of your previous responsibilities as an engineer- let your engineers have the wheel

## People Pleaser

- People pleasers are loved by everyone, believed to be the best manager in the world, and gets little done
- They also serve as blind spots for managers that manage managers, due to only hearing the good things until it's too late
- Characteristics of a people pleaser include:
  - Spends most of their time w/ 1-1s, and is involved w/ every little issue directly to solve them
  - Hides problems from team members
  - Prioritizes team smoothness and avoiding mistakes over pushing for excellence
  - Causes entire team to lose confidence when they're feeling down
  - Always has excuses for why work isn't done
  - Over promises and under delivers, and never learns from experience
  - Says yes to everyone and sends contradictory messages to both the team and external partners causing confusion
  - Seems to know all the problems in the company, but does nothing about them
  - Makes it impossible for the team to fail in a healthy way
- A competent manager will respect their layer of abstraction
  - Makes time for individuals when they request it
  - Spends time w/ management tasks like clarifying team objectives, making meetings smoother, running feedback between layers

## Preparing a Project

- W/o a project, a mentee is lost or bored
- If you're mentee is an intern, find something for them to work on for the first couple of weeks
- Figuring out a project otherwise is a tall order, but you can find a small feature of your own project that would take a few days to complete and start there
- After a mentee's on a project, break down tasks into milestones

## Process Czar

- Sometimes there are particular, knowledgeable, but inflexible engineers ("process czars")
- Characteristics include:
  - Believes that there's one true process that will solve all the team's biggest problems
  - Obsessed w/ Agile, Kanban, Scrum, Lean, or even waterfall methods
  - Very precise idea of how on-call should work, how code reviews should be done, how release process has to operate, etc
  - Organized and comfortable w/ details, and good at knowing/following rules precisely
  - Found in QA, help desk, or product management groups, and common in consulting agencies
  - Valuable members of project management due to making sure that no task is forgotten
  - Fail after realizing that others aren't as good at following processes as they are
  - Blames all problems on failure to follow processes instead of acknowledging need for flexibility and inevitability of unexpected changes
  - Focused on easy-to-measure things like hours in the office
  - Search for the "right-tools" to solve issues w/ planning, focus, time management, prioritization
  - Tries to stop all work while searching for the right process
- ...The "opposite" of a process czar:
  - Someone who understands that processes must meet the needs of the team and the work
  - Follows Agile to emphasize
    - Individuals and interactions over processes and tools
    - Working software over comprehensive documentation
    - Customer collaboration over contract negotiation
    - Responding to change over following a plan
- Process czars have room to get comfortable w/ ambiguity
- Clarify that it's safe to fail- there needs to be some tolerance to have all engineers fit together to follow any effective scheme to the best that they can

## Promotion

- Provided a company has some level of responsibility designation w/ respect to titles/roles, a manager needs to know whether an employee is qualified to be promoted
- An employee should have the qualities of a role they are being considered for before they're promoted
  - This is to avoid promoting engineers to their level of incompetence

## Questions To Ask a Mentee

- Good questions to ask a mentee include:
- How do you like to be praised, in public or in private?
- What's your preferred method of communication for serious feedback? In writing to digest it, or is less formal verbal feedback ok?
- Why did you decide to work here? What are you excited about?
- How do I know when you're in a bad mood or annoyed? Are there things that always put you in a bad mood that I should be aware of?
- Are there any manager behaviors that you know you hate?
  - Ie, skipping/rescheduling 1-1s, neglecting to give feedback, avoiding difficult conversations
- Do you have any clear career goals that I should know about so I can help you achieve them?
- Any surprises since you've joined, good or bad, that I should know about?
  - Where are my stock options? Where's my relocation bonus? Why are we using SVN instead of Git? etc

## Review Decision and Process Outcomes

- Discuss and review whether hypotheses were true and whether decisions were optimal
- Review processes and whether they're a good fit for the team, and revise accordingly

## Set Expectations

- Expectations need to be communicated clearly for a mentee to know what to do
  - If they should be able to look things up on their own, or spend some time trying something before asking, then tell them so
  - Be explicit when you expect a mentee to ask questions
  - Be explicit about your time commitments as an engineer and as a manager
- Worst case if a mentee fails even after repeated attempts to communicate, give them a project to work on for a day or two and see where they land

## Standards for Code and Systems

- By establishing a format for code and systems, you can de-personalize the process of providing technical feedback
- Includes amount of unit testing required, when technical decisions should be reviewed, etc

## Stay Out of Management Role As Needed

- Getting pushed out of technical work too early is dangerous
- After you have all technical skills down like the back of your hand, then you can move on to management
- Building technical know-how while also managing others is difficult

## Stay Technically Relevant

- Oversee technical investment
  - As a manager, your job is to weigh the need for different technical advances (new languages, frameworks, infrastructure, and features) and deploy provided the limited time and energy
- Ask informed questions
  - There's no need to run all the research or know what's best all the time
  - Guide the investments by asking questions:
    - What are the current projects, and what surprises/bottlenecks have they uncovered?
    - Which teams are asking for more engineers, and why do they think they need more people?
- Analyze and explain engineering and business tradeoffs
  - Engineers need to make decisions w/ an understanding of the business/product roadmap
- Make specific requests
  - Understand the progress of your team, the projects, and bottlenecks to filter out technically infeasible ideas and map new initiatives onto ongoing projects
  - When managers lag behind in technical knowhow, they'll become a go-between for senior management and their teams (which doesn't add any value)
- Use your experience as a gut check
  - To avoid investing time poorly (making poor leadership decisions), you need to stay technically relevant
  - That means:
    - Read code
      - Understand what's ugly and needs attention
      - Check code reviews and pull requests to know what work is being done
    - Pick something unfamiliar, and ask an engineer to explain it
      - If you're behind on how/why something is done, ask about it
    - Attend postmortems
      - After outages happen, attend the debriefs
      - You'll identify neglected/ignored standards, lack of communication, etc
      - You'll be caught up on the details of writing and deploying software too
    - Keep up w/ industry trends in software development processes
      - Managers often lose their touch for tools and processes for developing, testing, deploying, and monitoring code
      - Not every new software development/process trend is worth pursuing, but managers should know about them
    - Foster a network of technical people outside of your company
      - Being able to ask some people you trust about new trends is important
    - Never stop learning
      - Read articles and blog posts, watch talks, and learn about technology even if it's not directly applicable to work
      - Ask questions to your teammates

## The Larger Picture

- Employees need to be shown the larger picture when a project is mundane
  - ...it's also the employees job to make sure a manager knows that a project feels mundane as needed
- Mundane projects can be a source of pride when engineers know how they contribute to the larger goal of the company

## True North

- Refers to the core principles someone needs to keep in mind provided their job/role
- "true north" for each functional group is slightly different, which causes tension
  - Product might care about user experience over production support burden
  - Finance might care about overall cost of infrastructure over risks for availability
  - For startups, "structure" and "process" are seen as pointless at best and harmful at worst
    - ...When trying to introduce structure/processes, you can talk about learning and transparency instead of structure and processes respectively
- Risk analysis
  - W/ respect to some true north, risks are weighed and decisions are made
  - Below risks are considered "bad", but can be OK in some circumstances:
    - Having a single point of failure
    - Having known bugs and issues
    - Being unable to tolerate high load
    - Losing data
    - Putting out code that's undertested
    - Having slow performance

## Understand the Architecture

- You need to understand what the company is working on to lead others to work
- ...If you somehow made it to a management position w/o this technical understanding (or the company doesn't make it clear), prioritize it

## Virtues of Laziness/Impatience

- Laziness and impatience on their own are bad traits
- The two traits applied to processes and decisions is a good thing
  - We want to figure out what's important ASAP, and go home ASAP too
- As the saying goes, we need to work smarter, not harder
  - No one should be spending days and weeks (or their whole lives) employing brute force approaches instead of thinking about how life could be easier

## Warning Signs

- When you see below, they're warning signs that something's going on:
- Usually chatty, happy, and engaged, but starts leaving early, coming in late, takes breaks to leave during the workday, quiet during meetings, not hanging out on chat
  - Either not feeling well, or they're working on leaving
- Tech lead claims that everything is going well, but skips 1-1s and rarely provides detail in status updates
  - The tech lead is hiding something
- Team has no energy in meetings, except for tech lead and product manager
  - Shows that team doesn't feel any power in decision-making process
- Project list changes every week based on the customers' whim
  - Shows that the team hasn't thought about any goals beyond pleasing customers
  - There's a need for better product or business direction
- Small internal team seems fragmented in understanding
  - Profess ignorance on systems they don't work on, lack curiosity or openness to learn about other systems
  - Too identified by their day-to-day work, and resistant to change
