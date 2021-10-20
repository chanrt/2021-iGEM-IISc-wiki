# The relative path to the folder containing all your html files
relative_path = "src/"

# The file from which navbar and footer content should be obtained
source = "index.html"

# The files to which navbar and footer content must be injected from the source 
targets = []
targets.append("Attributions.html")
targets.append("Collaborations.html")
targets.append("Communication.html")
targets.append("Contribution.html")
targets.append("Description.html")
targets.append("Design_Solution.html")
targets.append("Design.html")
targets.append("EC_Education.html")
targets.append("EC_Communication.html")
targets.append("Engineering.html")
targets.append("Evaluate.html")
targets.append("Human_Practices.html")
targets.append("Ideate.html")
targets.append("Implementation.html")
targets.append("Judging.html")
targets.append("Members.html")
targets.append("Model.html")
targets.append("Model_Supplementary.html")
targets.append("Notebook.html")
targets.append("Parts.html")
targets.append("Predictions.html")
targets.append("Proof_of_Concept.html")
targets.append("Results.html")
targets.append("Safety.html")
targets.append("Sustainable.html")
targets.append("Template_page.html")
targets.append("Understand.html")

# navbar delimiters. Must be present in ALL the files listed in source and targets
navbar_start = "<!-- navbar start -->"
navbar_end = "<!-- navbar end -->"

# footer delimiters. Must be present in ALL the files listed in source and targets
footer_start = "<!-- footer start -->"
footer_end = "<!-- footer end -->"

# fetch navbar and footer content from source
source_file = open(relative_path + source, "r")
source_content = source_file.read()
navbar_content = source_content.split(navbar_start)[1]
navbar_content = navbar_content.split(navbar_end)[0]
navbar_content = navbar_start + navbar_content + navbar_end
footer_content = source_content.split(footer_start)[1]
footer_content = footer_content.split(footer_end)[0]
footer_content = footer_start + footer_content + footer_end
source_file.close()

for target in targets:
    # save pre-existing content from target page
    target_file = open(relative_path + target, "r")
    target_content = target_file.read()
    prenav_content = target_content.split(navbar_start)[0]
    middle_content = target_content.split(navbar_end)[1].split(footer_start)[0]
    postfoot_content = target_content.split(footer_end)[1]
    target_file.close()

    # insert navbar and footer content into target page
    target_file = open(relative_path + target, "w")
    target_file.write(prenav_content + navbar_content + middle_content + footer_content + postfoot_content)
    target_file.close()