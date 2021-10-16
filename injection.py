relative_path = "src/"
source = "index.html"
targets = ["Attributions.html", "Template_page.html", "Results.html", "Predictions.html"]

navbar_start = "<!-- navbar start -->"
navbar_end = "<!-- navbar end -->"

footer_start = "<!-- footer start -->"
footer_end = "<!-- footer end -->"

# fetch navbar and footer content
source_file = open(relative_path + source, "r")
source_content = source_file.read()

navbar_content = source_content.split(navbar_start)[1]
navbar_content = navbar_content.split(navbar_end)[0]

footer_content = source_content.split(footer_start)[1]
footer_content = footer_content.split(footer_end)[0]
source_file.close()

navbar_content = navbar_start + navbar_content + navbar_end
footer_content = footer_start + footer_content + footer_end

# print("NAVBAR CONTENT:")
# print(navbar_content)
# print("FOOTER CONTENT:")
# print(footer_content)

for target in targets:
    # save pre-existing content
    target_file = open(relative_path + target, "r")
    target_content = target_file.read()
    prenav_content = target_content.split(navbar_start)[0]
    middle_content = target_content.split(navbar_end)[1].split(footer_start)[0]
    postfoot_content = target_content.split(footer_end)[1]
    target_file.close()

    # print("PRENAV CONTENT:")
    # print(prenav_content)
    # print("MIDDLE CONTENT:")
    # print(middle_content)
    # print("POSTFOOT CONTENT:")
    # print(postfoot_content)

    # insert navbar and footer content
    target_file = open(relative_path + target, "w")
    target_file.write(prenav_content + navbar_content + middle_content + footer_content + postfoot_content)
    target_file.close()