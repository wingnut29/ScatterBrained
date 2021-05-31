Sub ScatterBrained()
	Dim oShell : Set oShell = WScript.CreateObject ("WScript.Shell")


	Dim folderName, file_name
	python_path = "venv\Scripts\pythonw.exe"
	file_name = "scatterbrained.py"

	Dim fso
	Set fso = CreateObject("Scripting.FileSystemObject")

	Dim fullpath, full_file_path
	fullpath = fso.GetAbsolutePathName(python_path)
	full_file_path = fso.GetAbsolutePathName(file_name)

	'WScript.Echo "folder spec: " & fullpath
	'WScript.Echo "full_file_path:    " & full_file_path


	'....continue....

	oShell.run "cmd /c " + fullpath + " " + full_file_path, 0, True
	Set oShell = Nothing
	
End Sub

	ScatterBrained()