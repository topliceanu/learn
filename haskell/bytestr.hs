import System.Environment (getArgs)
import qualified Data.ByteString.Lazy as B


copyFile :: FilePath -> FilePath -> IO ()
copyFile source dest = do
    contents <- B.readFile source
    B.writeFile dest contents

main = do
    (fileName1:fileName2:_) <- getArgs
    copyFile fileName1 fileName2
