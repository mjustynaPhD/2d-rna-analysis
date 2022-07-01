# Extract fasta from CIF (example)
`cd /data/2d-rna` <br>
`mkdir test` <br>
`cd test` <br>
`cp ../cifs/1FFK_1_0.cif .` <br>
`awk -f ../pre-preproc.awk < 1FFK_1_0.cif > 1FFK_1_0u.cif #dodaje pole  <br>"pdbx_formal_charge". Bez niego RNApdbee się wywala`
`conda activate pdbx` <br>
`cat 1FFK_1_0u.cif | ../preprocess-cif2.py > 1FFK_1_0-preprocessed.cif` <br>
`conda deactivate` <br>
`cd /home/macieka/2d-analysis` <br>
`sudo docker-compose run --rm --entrypoint ./rnapdbee rnapdbee -a DSSR -d VARNA -n ONLY_VISUALIZE -i /data/2d-rna/test/1FFK_1_0-preprocessed.cif -o /data/2d-rna/test/1FFK_1_0` <br>
`/usr/bin/gawk -v molecule_id=1FFK -f extract-2d.awk < /data/2d-rna/test/1FFK_1_0/0/whole.dbn > /data/2d-rna/test/1FFK_1_0.dbn` <br>
`/usr/bin/head -n2 /data/2d-rna/test/1FFK_1_0.dbn > /data/2d-rna/test/1FFK_1_0.fa` <br>

Implemented in /data/2d-rna/scripts/fasta-extraction/


# Prediction
`cd /home/macieka/2d-prediction/ <method>/predictions` <br>
`./predict.sh` <br>

# Convert predictions to bpseqs
`cd scripts/preds-to-bpseq` <br>
`./mxfold_bpseq.sh` <br>
...
`./rnafold_bpseq.sh` <br>
 
or `./pipeline.sh` <br>

# Validation
### Make directories for validation
`mkdir validation-all` <br>
`mkdir validation-noncanon` <br>
`mkdir validation-stacking` <br>

### Convert predictions from dotbrackets to bpseqs
`mkdir predictions-bpseqs` <br>

#### Convert from *.out to dotbrackets (mxfold, mxfold2, contextfold)
`/data/2d-rna/scripts/convert_dotbracket.sh ~/2d-prediction/mxfold2` <br>


#### Create bpseqs from all.csv and noncanonical.csv
`./make_bpseq_with_structure.sh` <br>

#### Copy canonical targets
`./copy_canonical_targets.sh` <br>

#### Filter predicted bpseqs with targets
`./filter_bpseq.sh`

#### RNA Validator
`java -jar rna2dValidator-1.0-SNAPSHOT-jar-with-dependencies.jar /data/2d-rna/validation-all/` <br>
`java -jar rna2dValidator-1.0-SNAPSHOT-jar-with-dependencies.jar /data/2d-rna/validation-canon/` <br>
`java -jar rna2dValidator-1.0-SNAPSHOT-jar-with-dependencies.jar /data/2d-rna/validation-noncanon/` <br>
`java -jar rna2dValidator-1.0-SNAPSHOT-jar-with-dependencies.jar /data/2d-rna/validation-pseudoknots/` <br>





