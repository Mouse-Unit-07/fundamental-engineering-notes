# What is Teamwork

- What is teamwork notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Correcting a Culture of Fear](#correcting-a-culture-of-fear)
- [Dysfunctional Teams](#dysfunctional-teams)
- [Dysfunctional Teams Resolutions](#dysfunctional-teams-resolutions)
- [Manage Conflict](#manage-conflict)
- [Measuring Team Health](#measuring-team-health)
- [Psychological Safety](#psychological-safety)
- [Toxic: Brilliant Jerk](#toxic-brilliant-jerk)
- [Toxic: Lacking Respect](#toxic-lacking-respect)
- [Toxic: Noncommunicator](#toxic-noncommunicator)

## Overview

> In many settings, your judgment and learning are calibrated by working alongside a more experienced partner: airline first officers with captains, rookies with seasoned cops, residents with experienced surgeons. The apprentice model is a very old one in human experience, as novices (whether cobblers or attorneys) have traditionally learned their craft from experienced practitioners.
>
> In other settings, teams are formed of people with complementary areas of expertise. When doctors implant medical devices like pacemakers and neural stimulators of the type that treat incontinence or the symptoms of Parkinson’s disease, the manufacturer has a product representative right in the operating room with the surgeon. The rep has seen many surgeries using the device, knows the kinds of patients that will benefit from it, knows the contraindications and adverse events, and has a hotline to the engineers and clinicians on the company’s staff. The rep tracks the surgery to make sure the device is implanted in the correct position, the leads are inserted to the correct depth, and so on. Every part of the team benefits. The patient is assured of an appropriate and successful surgery. The doctor gets product and troubleshooting expertise at her fingertips. And the company makes sure its products are used correctly.

- _Make It Stick: The Science of Successful Learning_

## Correcting a Culture of Fear

- > The culture of fear is pretty common in technology, and it survives best in environments where things are otherwise going well. Don’t be fooled by external circumstances that enable your bad behavior. If you’re feared but respected, the company is growing, and the team is working on interesting problems, you might get along OK for a time. However, if you lose any of these elements, you can expect to see people who have better options leave for greener pastures. I know firsthand that having a team that fears but respects you isn’t enough when they’re frustrated by other things happening around them. So work on softening your rough edges, practice caring about your team as humans, and get curious. Building a culture of trust takes time, but the results are well worth it.
  - Camille Fournier in _The Manager's Path_
- Practice relatedness
  - Focusing too much on efficiency is dehumanizing
  - Allow tolerance for small talk to see engineers as human beings
- Apologize
  - When you make mistakes, you need to apologize
  - Do so honestly and briefly
    - An ongoing apology turns into an excuse/distraction
  - Show others that it's safe to make mistakes, and that you should apologize when you hurt others
- Get curious
  - If you disagree w/ something, ask yourself and whoever is disagreeing why
  - If you mindlessly attack, people will evade/shut down, and learn that it's a good idea to hide information to avoid attacks and criticism
- Learn how to hold people accountable without making them bad
  - Not everything starts w/ responsibility and ends w/ consequences
  - Other elements include:
    - How success is measured, and whether the team has the capabilities needed to succeed
    - Providing feedback (just setting the goal clearly isn't enough sometimes)

## Dysfunctional Teams

- Characteristics include:
  - Missing deliverables
  - Unhappy engineers, engineers that keep quitting
  - Frustrated product manager
  - Team frustrated w/ product manager
  - Lacking energy in current work, or lacking enthusiasm in current projects
  - Something's wrong, but you can't tell what it is
- **Not shipping**
  - Caused by a lack of organization of tasks into smaller chunks, sorted to be done in parallel and in sequence if necessary
  - If a software team is slipping, then you're job as a manager is to go in and help to sort out the situation
  - Bad tools and processes need to be removed/revised
    - Infrequent releases reflect poor tooling around releases, heavily manual testing, features that are too big, and developers that don't know how to break down work
- **People drama**
  - If you have a "brilliant asshole", you either need to let them know that they're an asshole, or get them to leave
    - That person you think is productive and smart, but isn't a team player
    - Conversations w/ your manager and others is inevitable to resolve a brilliant asshole
  - Team members that dwell on negative experiences, spends too much time on gossip, and plays the us-against-them too much are harmful too
    - Just let them know how their behavior is affecting the team, and worst case help them leave the team
- **Unhappiness from overwork**
  - ...when problems aren't people related, it's easier to resolve
  - If there's overwork from the instability of production systems, then the manager has to slow down the product road map to focus on stability
  - Measure alerts, downtime, incidents, etc and work to minimize them
  - > My advice is to dedicate 20% of your time in every planning session to system sustainability work ("sustainability" instead of the more common "technical debt")
    - Camille Fournier in _The Manager's Path_
  - If it's overwork from time-critical releases:
    - Play cheerleader- help out w/ the work yourself, and show that you appreciate the work
    - Learn from the crunch period to avoid it next time- cut features, push back dates if it's unrealistic
    - ...crunch periods are inevitable, but they can be minimized
- **Collaboration problems**
  - Stay positive and supportive of each engineer's efforts in public even if you're frustrated w/ them
  - There's no quick fix to a complicated multi-team integration issue, but make sure to show willingness to improve collaboration
  - Have regular touch-bases w/ appropriate peers to work through issues
  - Encourage team members to get together outside of work to defuse the work-related tension

## Dysfunctional Teams Resolutions

- Fixing dysfunctional teams is a debugging process
  - There's a need to figure out "why things aren't working"
  - That's why high level managers need to be technically competent engineers
- Build a hypothesis
  - Go in w/ a hypothesis as to why a team is underperforming
  - Don't be overly invasive when trying to fix a team provided your hypothesis
- Check the data
  - Go ahead and check the logs- chats, emails, tickets, code reviews and check-ins
  - Are people sick? Are they fighting over coding style? Are tickets too big, vague, or too small?
- Observe the team
  - If a team is happy and not overburdened by production support, then it's time to get invasive
  - Join meetings- are meetings boring or ineffective?
    - Boring meetings signify lack of planning by managers accountable for organizing the meetings (redundant information covered, lack of direction, etc)
  - What's unfortunate is that your presence causes team members to change behavior
- Ask questions
  - Ask what the goals are to team members
  - ...Being unable to answer what project goals are shows manager incompetence in putting work into context
- Check the team dynamics
  - Are people friendly w/ one another?
  - Is there collaboration, or is everyone working independently?
- Jump in to help
  - After identifying any issues, troubleshoot the team dynamic
- Be curious
  - We learn from our mistakes by staying curious

## Manage Conflict

- Conflict is anything that causes a team to be dysfunctional (look into teamwork notes for details)
- Don't:
  - Rely exclusively on consensus or voting
    - Appears morally authoritative, but assumes that everyone is impartial, has equal stake on various outcomes, and has equal knowledge of the context
    - Undermines the minority at the cost of making a decision, which is cruel when there are better alternatives than public execution
  - Ignore simmering issues
    - Aka, inability to address issues until it's too late
    - When a manager gives negative feedback, it shouldn't be a major surprise for an employee
  - Take it out on other teams
    - A manager that avoids conflict in their own team may identify strongly w/ their own team, and conflict w/ other teams
    - Don't do that
  - Be afraid
    - Conflict arises from fear of consequences from making decisions, seeming too demanding, people quitting, being disliked, failure
    - Fear is natural, and being sensitive to outcomes of conflict is wise
- Do:
  - Set up clear processes to de-personalize decisions
    - Establish clear set of standards to evaluate decisions
    - Share a common understanding of goals, risks, and questions that need to be answered before making decisions
  - Address issues without courting drama
    - You want to allow space for people to express frustration, but address real interpersonal issues
    - It's not the manager's job to be a therapist, but it is to address dysfunctional teams
  - Remember to be kind
    - It's "nice" to:
      - Do things for others w/o expecting anything in return
      - Say "I'm fine" when you mean "I'm in a really crappy mood and I wish you would leave me alone"
    - It's "kind" to:
      - Tell someone that isn't ready that they're not ready for a promotion, and tell them what they're missing
      - Tell someone they're disrupting the team
  - Stay curious
    - Think about your actions to combat conflict- stay self aware

## Measuring Team Health

- By "health", it means both the sanity of engineers and how effective a development team is
- Measures are:
- Frequency of releases
  - > If your company doesn't appreciate the value of releasing code frequently, I'm sorry. In this modern era, frequency of code change is one of the leading indicators of a healthy engineering team. Great engineering managers of product-focused teams know how to create environments where their teams can move fast, and part of moving fast requires breaking work down into small chunks. Even if your company doesn't appreciate it, you must work to help your team achieve the best release frequency possible for their product.
    - Camille Fournier in _The Manager's Path_
- Frequency of code check-ins
  - Same as above
  - Engineers shouldn't be developing on their own for weeks without pushing it to shared version control
- Frequency of incidents
  - We all want to minimize incidents, but the key is to balance incident prevention and incident frequency such that developers aren't pulled away from working for days at a time
  - Methods of incident prevention are probably known- it's just a matter of how much time you spend at it
  - Weeks of manual QA, excessive/slow code reviews, infrequent releases, drawn-out planning processes, increased analysis, etc causes idle/restless developers

## Psychological Safety

- Team members need to feel safe to take risks and make mistakes in front of one another
- Employees should feel safe to joke together, get food together, and feel friendly towards one another
- Employees and managers that don't enforce this safety are "toxic", and creates dysfunctional teams

## Toxic: Brilliant Jerk

- Aka, that toxic employee that produces individually outsized results, but is so ego-driven that they create a mix of fear and dislike in almost everyone around them
- Similar to the alpha geek, but more aggressive
- Bullies w/ their intellect, cuts down dissenting voices in a harsh way, and lets out frustration w/ anything they see as stupid
- If you're this bad you probably don't have any facet to take any advice, but don't do this

## Toxic: Lacking Respect

- For whatever reason, an employee might not respect their teammates or manager
- If they do want to be working on the team, clarify expectations
- If they don't, then move them to another team or have them leave the company

## Toxic: Noncommunicator

- Refers to people that hide information from their team members and managers
- Prefers to work in secrete, and may unveil some magical project when everything is done and perfect
- Instead of talking to teammates, they revert others' commits, take their tickets, and does the work for others
- Doesn't like code reviews, and doesn't ask for design reviews on big projects
- Annoys everyone around them- don't do this it's toxic
- Often caused by the lack of psychological safety for failure
