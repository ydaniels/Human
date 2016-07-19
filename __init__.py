__author__ = 'root'
#
#run example
#sbf --sm=facebook --connection=api --action=follow --rule_file=frule --accfile=load.txt  --=accounts=1,2,3 --plugins=filter,machine,tensor
#sbf --sm=twitter --connection=web --action=unfollow --accfile=load.txt  --=accounts=1,2,3 --plugins=people_not_following
#action is just a step to perform action you have to provide data on what they are performing
#that is the what the how is provided bby the framework using rules
#use the plugins to manipulate  actions
#
#sm means load facebokk use the api for this connection perform follow action base on rules on frule file use accounts load.txt use spe
#cifi accounts apply this list of plugin to the operation
#
#
#
#
