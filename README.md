# SKIF 1-7 Beamline Controls (TANGO)

## Status 
TODO: create docs and have the project log there

### Before running anything --- synchronize DB

At the moment the only container that requires persistent data that is synced between developers and the beamline is MariaDB SQL-server.

The backups are stored in `db_backup` folder and in the same folder there is a synchronization script `sync.sh`. The backups are gzip archives labeled as `%volume name%_%commit hash%.tar.gz`. All `master` branch commits should have a corresponding DB backup.

In order to set up the DB, run `sync.sh`. If there is a backup for the current repo HEAD, the script will offer you to create a new docker volume from it.

After you have made changes to the codebase and the DB in the docker volume, commit your changes and run `sync.sh`. The script will offer you to create an archive and save it.

### Running the dev env

The whole beamline control system is emulated as a collection of Docker containers. `docker-compose up` launches the whole system, with the following components:
1. MariaDB SQL-server (Docker service `tango-db`).
2. TangoDB (Docker service `tango-dbds`).
3. Sardana server (Docker Service `sardana-srv`).
4. Optics Hutch control computer (Docker Service `ohcc01`). It will run XPS controller + two slit controllers.
5. Experimental Hutch control computer (Docker Service `ehcc01`). It will run Keithley controller for 3 picoampermeters + one slit controller.

To run the UI, specifically Jive, Astor, and Spock there are three docker-based scripts: `run-astor.sh`, `run-jive.sh`, `run-spock.sh`. Since Astor and Jive are written in java and are very easy to install, it is recommended to not use these scripts and just launch the apps locally after setting `TANGO_HOST=127.0.0.1:10000`.

## TODOs
1. Add secure password for MariaDB. (For now we literally have no production environment, so this is not important but needs to be fixed) 

2. Add health check to Sardana container

3. `tango-dbds` throws an error on startup `tango-dbds-1|device tango/admin/b8381df35a94 not defined in the database !`

4. Figure out logging. also where does `Device.info_stream()` write?

5. Add persistent storage where necessary.

6. Attach `db-backups/run-backup.sh` to commit hash and add restoring script also by commit hash.

## General plan
We should try to implement the following logic:
1. All Sardana controllers run together with Sardana server on the same container.
2. Sardana controllers wrap corresponding tango devices which act as drivers and are on their corresponding computers, such as OHCC01 and EHCC01.
3. All computers with Tango Devices on them are controlled by tango starter.

## Random knowledge
### Starter 
`Starter` device server provides Starter class. Instance name can be arbitrary, but the device names (1 device per physical host) have to be `tango/admin/%hostname%`.

