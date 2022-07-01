# Extract fasta from CIF (example)
cd /data/2d-rna
mkdir test
cd test
cp ../cifs/1FFK_1_0.cif .
awk -f ../pre-preproc.awk < 1FFK_1_0.cif > 1FFK_1_0u.cif #dodaje pole "pdbx_formal_charge". Bez niego RNApdbee się wywala
conda activate pdbx
cat 1FFK_1_0u.cif | ../preprocess-cif2.py > 1FFK_1_0-preprocessed.cif
conda deactivate
cd /home/macieka/2d-analysis
sudo docker-compose run --rm --entrypoint ./rnapdbee rnapdbee -a DSSR -d VARNA -n ONLY_VISUALIZE -i /data/2d-rna/test/1FFK_1_0-preprocessed.cif -o /data/2d-rna/test/1FFK_1_0
/usr/bin/gawk -v molecule_id=1FFK -f extract-2d.awk < /data/2d-rna/test/1FFK_1_0/0/whole.dbn > /data/2d-rna/test/1FFK_1_0.dbn
/usr/bin/head -n2 /data/2d-rna/test/1FFK_1_0.dbn > /data/2d-rna/test/1FFK_1_0.fa

Implemented in /data/2d-rna/scripts/fasta-extraction/


#Prediction
cd /home/macieka/2d-prediction/ <method>/predictions
./predict.sh

# Convert predictions to bpseqs
cd scripts/preds-to-bpseq
./mxfold_bpseq.sh
...
./rnafold_bpseq.sh
 
or ./pipeline.sh

# Validation
### Make directories for validation
mkdir validation-all
mkdir validation-noncanon
mkdir validation-stacking

### Convert predictions from dotbrackets to bpseqs
mkdir predictions-bpseqs

#### Convert from *.out to dotbrackets (mxfold, mxfold2, contextfold)
/data/2d-rna/scripts/convert_dotbracket.sh ~/2d-prediction/mxfold2


#### Create bpseqs from all.csv and noncanonical.csv
./make_bpseq_with_structure.sh

#### Copy canonical targets
./copy_canonical_targets.sh

#### Filter predicted bpseqs with targets
./filter_bpseq.sh

#### RNA Validator
java -jar rna2dValidator-1.0-SNAPSHOT-jar-with-dependencies.jar /data/2d-rna/validation-all/
java -jar rna2dValidator-1.0-SNAPSHOT-jar-with-dependencies.jar /data/2d-rna/validation-canon/
java -jar rna2dValidator-1.0-SNAPSHOT-jar-with-dependencies.jar /data/2d-rna/validation-noncanon/
java -jar rna2dValidator-1.0-SNAPSHOT-jar-with-dependencies.jar /data/2d-rna/validation-pseudoknots/





