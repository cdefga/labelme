file = getArgument();
// print(file);
imp = IJ.openImage(file);
// print(file.replace('.dcm', '.jpg'));
IJ.saveAs(imp, "Jpeg", file.replace('.dcm', '.jpg'))
imp.close();