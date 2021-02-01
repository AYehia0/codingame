read -r N

max=10000000
x=0
nums=()
for (( i=0; i<$N; i++ )); do
    read -r Pi
    nums[$i]=$Pi
done

#sorting the array
sort_array () { 
    local v="$1[*]" IFS=$'\n'; 
    read -d $'\0' -a "$1" < <(sort "${@:2}" <<< "${!v}"); 
    }

sort_array nums -n

 
# # sorts the array
# nums=($(for p in ${nums[@]}; do echo $p; done | sort -n))

len=${#nums[@]}

for (( i = 0; i < len-1; i++ ))
    do
        x=${nums[$i]}
        y=${nums[$i+1]}
        diff=$(( y - x))
        if [ $diff -lt $max ]
        then
            max=$diff
        fi
    done
 
echo $max
