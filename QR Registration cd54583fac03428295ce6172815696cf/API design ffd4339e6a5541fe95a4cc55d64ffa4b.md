# API design

## GET

/workgroups: Gives the created groups.

/workgroups/<group_id>: Gives the users’ name that are in the group.

/users: Gives all the users.

/users/<user_id>: Gives information of the user given.

/sessions: Gives all the sessions and their parameters.

/supervisers: Gives all the supervisers.

/supervisers/<superviser_id>: Gives the superviser’s information.

## POST

/workgroups/new: Creates a new group.

/users/new: Creates a new user.

/sessions/new: Creates a new session.

/supervisers/new: Creates a new superviser.

## PUT

/groups/<group_id>: Modifies the selected group.

/users/<user_id>: Modifies the selected user.

/sessions/<session_id>: Modifies the seleceted session.

/superviser/<superviser_id>: Modifies the selected superviser.

## DELETE

/groups/<group_id>: Deletes the selected group.

/users/<user_id>:  Deletes the selected user.

/sessions/<session_id>: Deletes the seleceted session.

/superviser/<superviser_id>: Deletes the selected superviser.