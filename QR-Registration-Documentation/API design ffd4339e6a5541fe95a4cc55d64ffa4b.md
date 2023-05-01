# API design

## GET

/v1/workgroups: Gives the created groups.

/v1/workgroups/<group_id>: Gives the users’ name that are in the group.

/v1/users: Gives all the users.

/v1/users/<user_id>: Gives information of the user given.

/v1/sessions: Gives all the sessions and their parameters.

/v1/supervisers: Gives all the supervisers.

/v1/supervisers/<superviser_id>: Gives the superviser’s information.

/v1/workgroups/<id_workgroup>/users: Gets users in a workgroup.

/v1/users/<id_user>/sessions: Gets user’s sessions.

## POST

/v1/workgroups/new: Creates a new group.

/v1/users/new: Creates a new user.

/v1/sessions/new: Creates a new session.

/v1/supervisers/new: Creates a new superviser.

## PUT

/v1/groups/<group_id>: Modifies the selected group.

/v1/users/<user_id>: Modifies the selected user.

/v1/sessions/<session_id>: Modifies the seleceted session.

/v1/superviser/<superviser_id>: Modifies the selected superviser.

/v1/sessions/user/<id_user>: Finishs user’s session.

## DELETE

/groups/<group_id>: Deletes the selected group.

/users/<user_id>:  Deletes the selected user.

/sessions/<session_id>: Deletes the seleceted session.

/superviser/<superviser_id>: Deletes the selected superviser.