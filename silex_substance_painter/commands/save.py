import substance_painter.project

################################################################
#
#       Example code from sub Painter api
#
#################################################################

# Check if a project is already opened:
if not substance_painter.project.is_open():
    print("No project is opened!")

# Check if the project needs to be saved at all:
if not substance_painter.project.needs_saving():
    print("There is nothing to save!")

# Save the project under the name "project1":
substance_painter.project.save_as("c:/Documents/project1.spp",
                                  substance_painter.project.ProjectSaveMode.Full)
# This should print "c:/Documents/project1.spp":
print(substance_painter.project.file_path())

# Change the name of the project to "project2":
substance_painter.project.save_as("c:/Documents/project2.spp")
# This should now print "c:/Documents/project2.spp":
print(substance_painter.project.file_path())

# Create a backup copy of the project:
substance_painter.project.save_as_copy("c:/Documents/project2-backup.spp")
# This should still print "c:/Documents/project2.spp":
print(substance_painter.project.file_path())

# Save the project incrementally
#(writing to project2.spp, and not project2-backup.spp):
substance_painter.project.save(substance_painter.project.ProjectSaveMode.Incremental)

# Create a template from the project:
substance_painter.project.save_as_template(
    "c:/Documents/Adobe/Substance 3D Painter/assets/templates/template.spt",
    "DefaultMaterial")