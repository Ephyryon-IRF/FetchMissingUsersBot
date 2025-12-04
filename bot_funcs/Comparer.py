from bot_funcs.sheetDataWithAPIkey import mainISheet
from bot_funcs.UsersInGroup import mainIGroup

async def Comparer(guild: dict[str, any]):
    sheet_data, duplicates = await mainISheet(guild["sheet"], guild["parameters"], guild["start_row"])
    group_data = mainIGroup(guild["group"])
    count = 0
    userNotInDatabase = {}
    for role, members in group_data['membersByRole'].items():
        notInDatabaseUsers = [
            m for m in members 
            if all(m['username'] != entry['username'] for entry in sheet_data)
            and not (m['roleName'] == "Party Chairman" and m['username'] != ["Penkuvsky"])
            and not (m['roleName'] == "Commander" and m['username'] != ["SpeeD5y"])
        ]
        if notInDatabaseUsers:
            if role in ["Owner", "Guest", "Party Supporter", "Holder", "Group Holder", "Supreme Marshal", "Chief Marshal", "Consul Marshal", "Marshal of the Mechanized Army", "Tsardom"]:
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