import requests as rq

mainInput = input("Please, provide your discord invite code: ")

request = rq.get(f"https://discord.com/api/v10/invites/{mainInput}?with_counts=true")
if request.status_code == 200:
    print("The provided server invite exists!")
    data = request.json()
    server_name = data['guild']['name']
    print("Server:", server_name)
    if 'inviter' in data:
        invited_by = data['inviter']['username']
        invited_by_id = data['inviter']['id']
        print("The person who invited you:", invited_by + ", " + invited_by_id)
    else:
        print("This invite has either no inviter, or is a public invite.")
    if data['guild']['nsfw'] == False:
        print("NSFW? no")
    else:
        print("NSFW? yes")
else:
    print("The provided server invite is either invalid, expired or the server doesn't exist.")

