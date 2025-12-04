from bot_funcs.sheetDataWithAPIkey import mainISheet
from bot_funcs.UsersInGroup import mainIGroup

async def Comparer():
    sheet_data, duplicates = await mainISheet()
    group_data = mainIGroup(5267416)
    count = 0
    userNotInDatabase = {}
    for role, members in group_data['membersByRole'].items():
        notInDatabaseUsers = [m for m in members if all(m['username'] != entry['username'] for entry in sheet_data)]
        if notInDatabaseUsers:
            if role not in ["Initiate", "Advocate"]:
                print(f"\nSkipping role: {role}")
                notInDatabaseUsers.clear()
                continue
            print(f"\nRole: {role} - Users not in database:")
            for user in notInDatabaseUsers:
                print(f"{user['roleName']} - {user['username']}")
                count += 1
            print(f"\nTotal not in database for role {role}: {len(notInDatabaseUsers)}")
            userNotInDatabase[role] = notInDatabaseUsers
            print("-" * 40)
    print(f"\nOverall total not in database: {count}")
    return userNotInDatabase, duplicates