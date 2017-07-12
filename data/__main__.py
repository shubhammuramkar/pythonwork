from argparse import ArgumentParser
from data_class import UserManager
# from zintergating.templates import get_template,changing_context

parser = ArgumentParser(prog="data")
parser.add_argument("type", type=str, choices=['view', 'message'])
#parser.add_argument("did_send", type=str, choices=['true', 'false'])
parser.add_argument('-id', '--user_id', type=int)
parser.add_argument('-e', '--email', type=str)
args = parser.parse_args()
print(args)
print(args.user_id)



if args.type == "view":
	print(UserManager().read_data(user_id = args.user_id,email = args.email))
elif args.type == "message":
	print(UserManager().UserMessage())

