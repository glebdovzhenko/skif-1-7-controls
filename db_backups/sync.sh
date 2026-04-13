#docker run --rm -v skif-1-7-controls_tango-db-dev:/data -v "$(pwd)":/backup ubuntu:resolute-20260108 tar -czf "/backup/tango-db-dev-$(date +%Y-%m-%d).tar.gz" -C /data ./

vprefix="bl-1-7-controls"
vtag="tango-db-dev"

cmt=$(git rev-parse HEAD)
echo "Repo at $cmt"

vname="${vprefix}_${vtag}"
fname="${vprefix}_${vtag}_${cmt}.tar.gz"
echo "Looking for file $fname"

if [ -f $fname ]; then
    read -p "File found, synchronize Docker volume? [y/n] " ans
    if [[ "$ans" == "y" || "$ans" == "Y" ]]; then
        echo "Received [$ans], syncing"
        if [[ -n "$(docker volume ls -q -f name=$vname)" ]]; then
            read -p "Volume $vname exists and will be overwritten, are you sure? [y/n] " ans
            if [[ "$ans" == "y" || "$ans" == "Y" ]]; then
                echo "Received [$ans], deleting volume"
                docker volume rm --force $vname
                if [ $? -ne 0 ]; then
                    echo "Deleting volume failed, exiting"
                    exit -1
                fi
                echo "Creating empty volume"
                docker volume create $vname
                if [ $? -ne 0 ]; then
                    echo "Creating volume failed, exiting"
                    exit -1
                fi
                echo "Restoring volume data from backup"
                docker run --rm -v "$vname":/data -v "$(pwd)":/backup ubuntu:resolute-20260108 tar -xzf /backup/"$fname" -C /data
                if [ $? -ne 0 ]; then
                    echo "Restoring volume failed, exiting"
                    exit -1
                fi
                echo "Done"
                exit 0
            elif [[ "$ans" == "n" || "$ans" == "N" ]]; then
                echo "Received [$ans], exiting"
                exit 0
            else
                echo "Received [$ans], command not recognized, exiting"
                exit -1
            fi
        else
            echo "Volume $vname not found, creating from $fname"
            echo "Creating empty volume"
            docker volume create $vname
            if [ $? -ne 0 ]; then
                echo "Creating volume failed, exiting"
                exit -1
            fi
            echo "Restoring volume data from backup"
            docker run --rm -v "$vname":/data -v "$(pwd)":/backup ubuntu:resolute-20260108 tar -xzf /backup/"$fname" -C /data
            if [ $? -ne 0 ]; then
                echo "Restoring volume failed, exiting"
                exit -1
            fi
            echo "Done"
            exit 0

        fi
    elif [[ "$ans" == "n" || "$ans" == "N" ]]; then
        echo "Received [$ans], exiting"
        exit 0
    else
        echo "Received [$ans], command not recognized, exiting"
        exit -1
    fi
else
    read -p "File not found, create backup from Docker volume? [y/n] " ans
    if [[ "$ans" == "y" || "$ans" == "Y" ]]; then
        echo "Received [$ans], creating backup"
        if [[ -n "$(docker volume ls -q -f name=$vname)" ]]; then
            echo "Volume $vname exists, backing up"
            docker run --rm -v "$vname":/data -v "$(pwd)":/backup ubuntu:resolute-20260108 tar -czf "/backup/$fname" -C /data ./
            echo "Done"
            exit 0
        else
            echo "Volume $vname not found, exiting"
            exit -1
        fi

    elif [[ "$ans" == "n" || "$ans" == "N" ]]; then
        echo "Received [$ans], exiting"
        exit 0
    else
        echo "Received [$ans], command not recognized, exiting"
        exit -1
    fi
fi
#Then, create the empty volume (important!):

#docker volume create nextcloud_data
#Run the import command (from the folder containing the backup file):

#docker run --rm -v nextcloud_data:/data -v "$(pwd)":/backup ubuntu \
#  tar -xzf /backup/nextcloud-data-2025-04-05.tar.gz -C /data

