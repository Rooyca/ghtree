
def parse_markdown(data: str):
    """
    Parse markdown data and return a dictionary
    """
    data = data.split("\n")
    user_data_final = {}
    for line in data:
        if line.startswith("<!--"):
            continue
        if line.startswith("#"):
            key = line.replace("#", "").strip().lower()
            user_data_final["username"] = key
        if line.startswith("- profile-picture:"):
            user_data_final["profile_picture"] = line.replace("- profile-picture:", "").strip()
        if line.startswith("|"):
            key, value = line.replace("|", "").split(":")
            user_data_final[key.strip()] = value.strip()
        if line == "--- Bio ---":
            user_data_final["bio"] = ""
            for line in data[data.index("--- Bio ---") + 1:]:
                if line.startswith("<!--"):
                    continue
                if line.startswith("--- "):
                    break
                user_data_final["bio"] += line
                # check if bio is larger than 300 characters
                if len(user_data_final["bio"]) > 300:
                    user_data_final["bio"] = user_data_final["bio"][:300] + "..."
                    break
        if line == "--- Profile Items ---":
            user_data_final["profile_items"] = []
            for line in data[data.index("--- Profile Items ---") + 1:]:
                if line.startswith("--- "):
                    break
                if line == "":
                    continue
                if line.startswith("<!--"):
                    continue
                line_parsed = line.split("](")
                desc = line_parsed[0].replace("- [", "").replace("* [", "").strip()
                url = line_parsed[1].replace(")", "").strip()
                user_data_final["profile_items"].append({"desc": desc, "url": url})
        if line == data[-1]:
            break

    return user_data_final