import os

class FileSystem():

    def getFiles(self, path):
        files = []
        (root, dirNames, fileNames) = next(os.walk(path))

        dirNames.sort()
        for dirName in dirNames:
            files.extend(self.getFiles(os.path.join(root, dirName)))


        fileNames.sort()
        for fileName in fileNames:
            files.append(os.path.join(path, fileName))
        
        return files
