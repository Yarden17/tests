To use this module functionality you just need to:

On `project.project` level:

In Kanban View:

1.  Go to Project \> Dashboard
2.  Create
3.  Enter project name and use auto generated key or simply override
    value by entering your own key value.

In Tree View:

1.  Go to Project \> Configuration \> Projects
2.  Create
3.  Enter project name and use auto generated key or simply override
    value by entering your own key value.

In form View:

1.  Go to Project \> Dashboard
2.  Open the projects settings
3.  Modify the "key" value
4.  After modifying project key the key of any existing tasks related to
    that project will be updated automatically.

When you create a project, under the hood a ir.sequence record gets
creted with prefix: `<project-key>-`.

On `project.task` level:

1.  Actually there is nothing to be done here
2.  Task keys are auto generated based on project key value with per
    project auto incremented number (i.e. PA-1, PA-2, etc)

In browser address bar:

1.  Navigate to your project by entering following url:
    <http://>\<\<your-domain\>\>/projects/PROJECT-KEY
2.  Navigate to your task by entering following url:
    <http://>\<\<your-domain\>\>/tasks/TASK-KEY
