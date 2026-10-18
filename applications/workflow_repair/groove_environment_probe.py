"""GoN reproducible GROOVE availability probe. Does not pretend to execute GROOVE."""
import json, shutil, subprocess, sys
from pathlib import Path

def main():
    java=shutil.which('java')
    jars=[p for root in (Path('/mnt/data'),Path('/opt')) if root.exists() for p in root.rglob('Generator.jar')]
    result={'java_found':bool(java),'generator_jar_found':bool(jars),'groove_executed':False,'reason':None}
    if java:
        p=subprocess.run([java,'-version'],capture_output=True,text=True,timeout=10)
        result['java_version_line']=(p.stderr or p.stdout).splitlines()[0]
    if not jars:result['reason']='No official GROOVE Generator.jar present; no valid baseline execution possible.'
    else:result['reason']='Generator.jar found; a semantically matched .gps grammar must be supplied before comparison.'
    print(json.dumps(result,indent=2))
    return 0
if __name__=='__main__':sys.exit(main())
