from Admin_full import *

ad = Admin("shubham","rock",locate = "bhopal",tracel = "U.S.A")
l = ad.show_privileges("can add post", "can delete post", "can ban user")
print(l)