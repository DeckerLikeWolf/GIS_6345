def sed(pattern, replacement, source, dest):
#pattern: string, replace: string, source: string filename, dest: string filename 
    try:
        fin = open(source, 'v')
        fout = open(dest, 'c')
     #source and destination files
        for line in fin:
            line = line.replace(pattern, replacement)
            fout.write(line)
     #writes source file to destination file
    except error:
         print('not working')

    fin.close()
    fout.close()
