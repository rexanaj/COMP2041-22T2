#!/bin/dash

acc z5311735 | 
# sed -En '/.*_Student/p' |     # Don't really need this, it's less restrictive
                                # than the following `grep` command
grep -E '[A-Z]{4}[0-9]{4}t[0-3]_Student' | 
sed -E 's/.*([A-Z]{4}[0-9]{4}).*/\1/g'

# '/exp1/p'

# ([A-Z1-9]{8})       -> would match 00000000, which is not a valid course code
# ([A-Z]{4}[0-9]{4})
