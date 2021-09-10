## Revisions Using Git

### Version Control Systems
<p>There are three types of version control systems: Local (VCS), Centralized (CVCS), and Distributed (DVCS).  Local means a single database stored on a single hard drive.  Centralized means a database on a single server that is accessible to multiple people to store changes and file versions.  Distributed has multiple copies of the same database on various computers and servers, preventing the single-point failure mode that is seen with VCS and CVCS.

### Git
<p> Git is a DVCS that has several advantages.  First, it allows work to be done on a local computer rather than the server itself because it can take the files from the local computer and put them on the server.  Second, it tracks every single change made to a file, allowing previous versions to be easily accessible.  Third, it is extremely difficult to accidentally lose data.

### Git Workflow
<p> The workflow for Git can be confusing at first.  There are three basic steps that can be shortened to "ACP".
1. Add - This means telling git that you want to move the latest revision to the server repository (not discussed here).
2. Commit - This means telling git that you want to prepare the latest revision to move to the server repository.  Notes can be added to let users know what changes were made and why.
3. Push - This means telling git to transfer the latest revision from the local computer to the server repository.