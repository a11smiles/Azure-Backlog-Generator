import os

class FileSystem():

    def getFiles(self, path):
        files = []
        (root, dirNames, fileNames) = next(os.walk(path))

        fileNames.sort()
        for fileName in fileNames:
            if fileName == 'metadata.json':
                files.append(os.path.join(path, fileName))

        dirNames.sort()
        for dirName in dirNames:
            files.extend(self.getFiles(os.path.join(root, dirName)))

        return files
