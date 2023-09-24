# Project Name - README

## File Transfer Using SFTP

This README provides step-by-step instructions on using the SFTP command-line tool to perform file transfer in your project. These instructions will help reviewers understand how the file transfer was performed using SFTP. Please follow the steps below:

### Prerequisites

Before proceeding, ensure that you have the following prerequisites:

1. SFTP command-line tool installed on your local machine.
2. Access credentials (hostname, username, and password) for the sandbox environment.

### Establishing SFTP Connection

1. Open a terminal or command prompt on your local machine.

2. Use the following command to establish an SFTP connection to the sandbox environment:

   ````shell
   sftp username@hostname
   ```

   Replace `username` with your actual username and `hostname` with the provided hostname or IP address for the sandbox environment.

3. You will be prompted to enter the password associated with the provided username. Enter the password when prompted.

4. If the connection is successful, you will see an SFTP prompt indicating a successful connection.

### Navigating Directories

Once connected to the sandbox environment via SFTP, you can navigate to the desired directory using the `cd` command. Use the following command:

```shell
cd directory_path
```

Replace `directory_path` with the actual path to the directory where you want to upload the files. For example, if you want to navigate to a directory named "screenshots," use:

```shell
cd screenshots
```

### Uploading Files

To upload files from your local machine to the sandbox environment, follow these steps:

1. Ensure that you are in the desired remote directory where you want to upload the files.

2. Use the `put` command to upload files. The basic syntax is:

   ````shell
   put local_file
   ```

   Replace `local_file` with the path to the file on your local machine that you want to upload. You can use wildcards (*) to upload multiple files at once. For example, to upload all files starting with "screenshot" and ending with ".png" in the current local directory, use:

   ````shell
   put screenshot*.png
   ```

3. After executing the `put` command, the file(s) will be uploaded to the remote directory on the sandbox environment.

### Verifying File Transfer

To verify that the file(s) have been successfully transferred to the sandbox environment, you can use the `ls` command. The `ls` command lists the files and directories in the current remote directory. Use the following command:

```shell
ls
```

This will display the files and directories in the current remote directory. Verify that the uploaded file(s) are present in the list.

### Additional Notes

- Make sure to replace the placeholder values (e.g., `username`, `hostname`, `local_file`) with the actual values specific to your setup.

- It is recommended to include these instructions and command examples in your project's `README.md` file for easy reference.

- Provide clear and concise instructions in your `README.md` file to help reviewers understand the steps you followed to use the SFTP command-line tool for file transfer.

- If you encounter any issues during the file transfer process, make sure to include troubleshooting steps or error messages in your `README.md` file for better understanding and resolution.

By following these steps, you will be able to use the SFTP command-line tool for file transfer in your project.
