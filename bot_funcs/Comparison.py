from bot_funcs.Comparer import Comparer

async def Comparison():
    notInDatabase, duplicates = await Comparer()
    result = []
    for role, users in notInDatabase.items():
        print(f"\nRole: {role} - Users not in database:")
        for user in users:
            print(f"{user['roleName']} - {user['username']}")
            result.append(f"{user['roleName']} - {user['username']}")
    print(f"\nOverall total not in database: {len(result)}")
    if not result:
        result.append("All users are in the database.")
    result.append("-"*40)
    result.append("**Duplicates found in sheet data:**")
    for dup in duplicates:
        result.append(dup)
    joined = "\n".join(result)
    return joined