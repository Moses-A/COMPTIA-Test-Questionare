#Simple Multiple Choice Questionare   
# Written by Moses Arocha

$Entry_message = " Welcome To The Linux Questionare"
$answer = " Would You Like To Go Over Notes? "

$yes = New-Object System.Management.Automation.Host.ChoiceDescription "&Yes","Preparing Notes..."
$no = New-Object System.Management.Automation.Host.ChoiceDescription "&No", " Preparing Exam Questions"

$options = [System.Management.Automation.Host.ChoiceDescription[]] ($yes, $no)

$result = $host.ui.PromptForChoice($Entry_message, $answer, $options, 0)

switch ($result)
{
    0 {
        $notes = Get-Content "C:\Users\localhost\Documents\Linux+\Help Facts.txt" | ForEach-Object {Get-WmiObject -computername $_ win32_bios}

    }

    1{
        
        

    }
}
