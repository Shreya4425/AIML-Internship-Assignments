raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users = set(raw_logs)

print("Is ID05 present?", "ID05" in unique_users)

print("Total IDs in raw logs: ", len(raw_logs))
print("Unique IDs after removing duplicates: ", len(unique_users))

print("Unique user IDs: ", unique_users)
