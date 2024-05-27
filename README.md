# Django_project
Building To-do list web app using Django web framework

## API Endpoints

### List all tasks
**GET** `/api/`

Retrieves a list of all to-do tasks.

### Get task details
**GET** `/api/<int:pk>/`

Retrieves details of a specific task by its ID.

### Create a task
**POST** `/api/create/`

### Update a task
**PUT** `/api/<int:pk>/`

### Delete a task
**DELETE** `/api/delete/<int:pk>/`

Deletes a specific task by its ID.

