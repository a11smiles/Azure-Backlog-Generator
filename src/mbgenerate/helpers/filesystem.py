import os

class FileSystem():
    parentPath = True

    def getFiles(self, path):
        files = []
        (root, dirNames, fileNames) = next(os.walk(path))

        if self.parentPath == True and len(fileNames) > 0:
            raise FileExistsError("parent path should not contain any files")
        elif self.parentPath == False and 'metadata.json' not in fileNames:
            raise FileNotFoundError(f"'metadata.json' does not exist in path '{path}'")

        fileNames.sort()
        for fileName in fileNames:
            if fileName == 'metadata.json':
                files.append(os.path.join(path, fileName))

        self.parentPath = False

        dirNames.sort()
        for dirName in dirNames:
            files.extend(self.getFiles(os.path.join(root, dirName)))

        return files
