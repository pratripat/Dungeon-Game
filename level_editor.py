from Level_Editor.scripts.editor import Editor

def main():
    #Runs the editor
    editor = Editor()
    editor.load('data/levels/5.json')
    editor.main_loop()

main()
