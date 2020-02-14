JMeter Learning


How to create Jmeter test:

Start JMeter
Create a TestPlan
Create a Thread Group (Users)
Add a Sampler (e.g HTTP request)
Add Listeners to view the results like “View Result Tree”, “Asserion Results” etc
Run the Test


1: Assertions:

Assertion = check on the Response 

E.g check the 
size of the response
time of the response 
Duration of the response



Response Assertion: >> to check the response code of the result
Duration Assertion >> to put a limit on the time of the response
Size Assertion >> to put a limit the size of the response
xPath Assertion >> mostly used in API testing  >> to check particular Node or xpath in response >> not used yet


2: Listeners:

Listener = elements that gather information about the performance test.

>> Used to view results / metrics of the test


Latency = time to first byte of the response after request is sent to some server
Response time = time when complete response is received
Connect Time = the time the request took to connect to the server 
Aggregate Report >> Listener that gives single line result for one sampler.
Graph Results >> Listener that gives a run-time graphical representation of the response KPIs (Highly memory consuming listener)
Simple Data Writer >> Listener that saves the results in a file with configuration button with option what to save and what not in that file. >> Best to use this while doing load testing of a server. >> not used myself




Note:

1: Listeners e.g View Results Tree take up a lot of memory. When doing load testing, better is to disable most of the listeners but if you are checking/validating the application, you can use them.
2: All the data of the listeners can be saved in a given file type on your system by giving the filename

=======

Logic Controllers:

They are used to make grouping of different elements e.g samplers on the basis of their similarities.

1: Simple Controller (Do nothing controller)
	It is the controller which is not to perform any task but just to do grouping simple requests together. E.g Login, registration, search and logout is the test scenario containing 20-30 requests.
We can use Simple Controller to separate all these requests in 4 separate groups.

2:  Loop Controller
	In order to execute some particular request/requests in a given test case (thread group) x number of loops instead of running all
the requests x number of times, we use Loop controller and put that speicific request (sampler) inside the Loop controller and give
the count value in it.

3: Random Controller
	Whenever we want to execute anyone of the available requests, we put the multiple requests in the Random Controller and it will run anyone of the available
requests (samplers).It executes only one child given in it randomly.

4: Random Order Controller
	It is a controller which send the requests which are added in it as a child in Random order e.g if three requests are added in Random Order Controller, it 
may send the request in 1,2,3 fashion or 2,1,3 or 3,1,2 or the other. While the Simple Controller sends the requests only in a way they are added in the controller tree.

5: Interleave Controller
	It is a controller that executes only one of its child request in each loop of the test cases (Thread group) but 
in sequence as they are added in the controller. e.g if 1,2,3 requests are added and test cases is run for 4 loops, the sequence of the 
execution will be 1,2,3,1.

6: Module Controller
	It is a controller used to call other controllers in the same test case (thread group) or in any other test case. So, this controller there for reusing the same
controller in our test plan instead of writing it again and again. It is just like calling functions in coding.

============


Pre Processors:

These are the jmeter elements that are used to execute actions before the sampler requests are executed in a test plan.
A Pre-Processor is most often used to adjust the settings of a Sample Request just before it runs.


1: HTML Link Parser
	A preprocessor that uses the response of HTTP request1 and extracts the data (links) out of it to be used futher requests in a test plan.
For example if we want to hit all the links of a website, we add HTTP Request (with Home page and path as ".*" to pick a random link from the first response), add HTML link Parser as child and run. It will execute all the
links available on the Home page and hit all of them.>> Used in file Pre_Post_Processors.jmx

2: Users Parameters
	Users Parameters allows the user to specify values for User Variables specific to individual threads. Parameters Pre-Processor can be used to set different parameters for each simulated user. When only one user is defined, 
this value will be used for all threads. For this define "Parameters Name" in the PreProcessor and give values to "User_1,User_2 etc". After that, add Parameter Name with value as "${parameter_name defined in PreProcessor}". Set the No. of Users 
in Thread group equal to number of Users in PreProcessor.

3: SampleTimeOut PreProcessor
	The PreProcessor that is used to check the Sample Time of the Request. If the sample time of the request goes beyond the given value in 
PreProcessor, the Status of the request will be shared as Fail. This PreProcessor works same as Time Assertion in Jmeter.

=========


Post Procesors:

1: BeanShell PostProcessor
	It is a post processor that needs BeanShell scripting for specific set of instructions in a test plan. >> It will be done later in Jmeter learning

2: Regular Expression Extractor (RE Extractor)
	
	Correlation >> The process of 'extracting' some value from the response of one request and 'referring' it into the request of the later requests in test plan. For example in Login > HomePage > Logout type test plans,
we get a session ID and this session ID is generated after login request, and is need in upcoming request of Homepage etc. Here we need Correlation.

	RE Extractor is a Post Processor which is used to work on Response Body/Headers of the request by using Regular Expression search format. A variable is created
in a RE Extractor and the match cases are stored in it. That variable can be used further in a test plan as needed. Worked on Google.com webpage, extracted the links there
by using RE and further used that in the next http request.

3: Xpath Extractor
	Similar to RE Extractor, XPath Extractor is also works on Response of one request, search some values using XPath Querry (special format), put the value in some variable 
and use it in further test plan. XPath Querry is quite similar to json path querry but it will need some effort to master this querry language.


========


Assertions in Jmeter:
	Assertions are the checkpoints put on the response of the request to see if the required result is acheived or not. There is also a Listener designed to check the results of the Assertions i.e
"Assertion Results".

1: Size Assertion >> used to put a check if the response of the request is within the described size in Bytes
2: Duration Assertion >> used to put a check if the response of the request is received within the described timeline in mili-seconds
3: HTML Assertion >> Used to check if the response of the request is of the correct formats like HTML/XHTML/XML with given number of Error and Warnings in the format. The certain number of Errors and Warnings can be allowed as minimum to pass the 
test case.
4: Response Assertion >> It is the assertion put on Response Code, Response Text, Response Message etc to match with a given value. If the request's response matches with the test value, the assertion result will pass, else Fail. 
5: JSON Assertion >> If some request has json as response, you can validate your response result using JSON Assertion. The Json path to be given in assertion can be created using 
the JSON Path Tester in Response Tree listener first and then puting it in assertion.


=========

Config Elements:
	Configuration elements can be used to set up defaults and variables for later use by samplers. 
Note that these elements are processed at the start of the scope in which they are found, i.e. before any samplers in the same scope


1: HTTP Header Manager
	This is the config element that is used to parse any Header from Header Manager of any http page. The required Header name and value can be found by using "Inspect" in browser and looking under Network-Headers-Request Headers.
Used this Config Element to parse Cookie for Gmail Account creadentials required to access Ctech Attendance portal.

2: HTTP Cookie Manager
	This is the config Element that is used to use cookies of some http request afer the first iteration. In 2nd loop and onwards, if there are cookies that are used in request 1, they will be used in 2nd loop http request (can be seen in Request Body under
the Cookie Data heading). This is used for better user experience. Used this Cookie Manager at the end of a Thread Group to save the Cookies (used for Authentication of Ctech Attendance Portal). Put the First Request in "Once Only Controller" with use of HTTP Header 
Manager in the first request to give access. Put all the request down in the flow, outside the controller, they will all now run successfully using the cookie stored in Cookie Manager.

3: HTTP Cache Manager
	It is used to simulate the browsers caching behavior of files like HTML, CSS, JavaScripts and graphic images in Jmeter. In revisit on browser or 2nd loop request in jmeter, now the cached content will not be re-downloaded reducing the bandwidth on both server and user sides.
It also allows the page to load faster and in Jmeter scenario is same as it happens in real time. For cached data in any HTTP request, go to "Advanced" options and enable "Retreive all Embedded Resources". Run your Request for multiple number of loops and observe the Sample Time and Received Bytes
in Listener to get the difference of the caching.

4: Counter
	It is a config element that can be used for handling scenarios where we need to use incrementing/decremeting value in multiple requests. We use counter, save its value in some variable and use that
variable in our requests.

Custom Assertions:
	Added JSR223 Listener in the HTTP Request, added some groovy lines code to update the AssertionResult message to some custom message. Also used the Assertion Result Listener and used it to save the Response params in CSV for Success and Failure cases. 
Still to figure out if Assertion Success Message can be printed and modified.


Stress Testing and Planing: 

Process of verifying and validating a software is called a Software Testing.

Types of Software Testing:
a: Functional Testing
b: Non-Funtional Testing

Types of Functional Testing:
1: Unit testing
2: Integration testing
3: System testing
4: Interface testing
5: Regression testing
6: User Acceptance testing

Types of Non-functional Testing:
1: Documentation testing
2: Installation testing
3: Performance testing
4: Reliability testing
5: Security testing

Now Types of Performance Testing:
1: Load testing
2: Stress testing
3: Endurance testing
4: Spike testing
5: Scalibility testing
6: Volume testing

Stress Testing:
	The type of performance testing in which we overload (even beyond the evaluation points) the system and system response is monitored to ensure that the system can sustain the stress. Also known as Endurance testing, it gives us the
limit of the system till which it will work. It is done to be prepared for the worst conditions.

Types of Stress Testing:
1: Distributed Stress Testing >> over the client and servers separately
2: Application Stress testing >> related to defects in data loging, blocking, network issues and other related bottlenecks
3: Systematic Stress testing >> by running multiple systems on the same server. It can be used to test where one application data blocks the other application. 

How to Perform Stress Testing: (Tools are Jmeter/Neoload(web + mobile apps)/Load Runner(by HP))
1: Planing
2: Create Automation script
3: Execute the script (test plan)
4: Result Analysis
5: Optimization and fine tuning of the system

Usually 3-4 cycles are executed and system is optimized.

Non-GUI Mode of Jmeter:

Go to bin folder of your JMeter installation from command prompt and type the following command
	jmeter -n -t D:\TestScripts\script.jmx -l D:\TestScripts\scriptresults.jtl
	On remote Linux Machine command is >> sh jmeter.sh -n -t test.jmx -l log.jtl
where
-n [This specifies JMeter is to run in non-gui mode]
-t [name of JMX file that contains the Test Plan]
-l [name of JTL(JMeter Text Logs) file to log sample results to]
-j [name of JMeter run log file]

For Stress Plan task:

Created a test plan for stress testing of Ctech Attendance portal.

Used Cookie Manager to set Cookie data in Request that are put in loop. 
Used Retrieve all Embedded Resources to mimic the browser 
Used Cache Manager to do caching of resources like browser
Put 10 users in a loop of 10 with Ramp-up Period of 5 seconds (that can be increased if needed)
Disabled the Listeners in jmx file and saved


For Non-GUI mode:

Go to bin folder of your JMeter installation from command prompt and type the following command
	jmeter -n -t testplan_shahid\Config_Elements.jmx -l testplan_shahid\Config_Elements.jtl

Run the testplan in non-Gui mode and saved the results in .jtl(jmeter text logs) format. Further used that log file to generate the following by using loading the jtl file in the Listeners
Response Time Graph.png 
Aggregate Report.csv

=======

Jmeter Dashboard Report:

To generate the html file with most of the data in presentable format, use this
https://jmeter.apache.org/usermanual/generating-dashboard.html

To generate Dashboard Report,

1: Go to user.properties file in "bin" folder and set
>>> jmeter.save.saveservice.output_format=csv

2: In command line, use the format
jmeter -n -t examples\Shahid\HOBBS_QA_api.jmx -l examples\Shahid\result-feb.csv -e -o Feb-results

-e = to continue working anything after the test run is complete
-o = to give hte Folder name that needs to be created in "bin" folder where the html Dashboard report will be created

=========

CBL APIs Testing:

Defined HTTP Headers in Config Element "User Defined variable" above the thread group. 
Used those variables in all the https request's "Header Managers" further in test plan
Used JSON Assertion to validate the json response of each https call
Used "http://jsonpathfinder.com/" to find the the "JSON Path" for a particular field in json response
 


Text Moderation with Fizz/CleanSpeak

Beanshell script:

1: How to print some local variable (defined in beanshell) on console >> 

System.out.println("Payload:[" + payload + "]");
System.out.println("Authorization:[" + Authorization + "]");

2: How to print some local variable (defined in beanshell) in Jmeter logs >>

log.info("Payload: " + payload);
log.info("Authorization: " + vars.get("Authorization"));

3: How to take beanshell variable out to jmeter test plan >> here Auth1 is local beanshell variable which is going to be saved
in "Authorization" which can be referenced in test plan using ${Authorization}

String Auth1 =  new String (hash, StandardCharsets.UTF_8);
vars.put("Authorization","HMAC-SHA256 " + Auth1);
	
4: How to take the sampler request body into beanshell script >>

String payload = sampler.getArguments().getArgument(0).getValue();


Task1: A: Identify the parameters/variables that are important

>> Authorization key that is required to create a user session
>> User session created will generate "token" and "subscriber_id" in response 
>> The session_token will be used in https://api.fizz.io/v1/moderatedTexts API with sample text body
>> Response of the API will replace the profane words with * (done by CleanSpeak)

To pass a variable from one thrread group to anouter in jmeter >> yet to test

///
if you are reading from a variable

import org.apache.jmeter.util.JMeterUtils;
JMeterUtils.setProperty("PC_CREATED_PROMO_CODE", vars.get("Extracted_PC_CREATED_PROMO_CODE"));
And then from the other thread group, read it via (http://jmeter.apache.org/usermanual/functions.html#__property)

${__property(PC_CREATED_PROMO_CODE)}
///

GOTO Statement:

The aim of a GOTO statement is to perform a reassignment to another line of code. In other words, the GOTO statement is very useful 
when you need to jump to another part of the flow, which is usually identified by a particular label.


>> Add the If Controller below the request where you need to check and reassign to somewhere
	> ${JMeterThread.last_sample_ok}==true is a function that returns true or false depending whether the last sample "response" was OK or not
	> Multiple conditions in If Controller > AND = &&, OR = ||


Throughput Controller:

This controller is not there to control throughput instead it defines how often its child elements are executed. It allows you to setup the user load for different requests in a single 
thread group.

There are two options i.e 

1: Total Executions >>  defines how many times the child elements will be executed (absolute number)
	1(a): If “Per User” is unchecked >> the underlying sampler(s) will be executed as many times as defined in the “ThreadGroup” field
		e.g Thread Group users = 100, Throughput field value = 100 >> test elements will be executed 100 times

	1(b): If “Per User” is checked >> child sampler(s) will be executed as many times as defined in the “Throughput” field
		e.g Thread Group users = 100, Throughput field value = 200 >> test elements will be executed = 200 times

2: Percent Executions (Uncheck per user checkbox)>> the child elements will be executed according to the percentage of iterations (threads * loops) as defined in the “Throughput” field
		e.g Thread Group users = 100, Loops = 3 Throughput field value = 10.0 (%) >> test elements will be executed 10% of 300 = 30 times
	
Important: If we put the Throughput Controller and its request body inside the "Runtime Controller" >> through put is higher than one that is calculated
		

Throughput is controlled by using "Constant Throughput Timer" at the start of the thread group. It will control the Throughput (TP) with Multiple users in ThreadGroup.


How to Configure Logging:

Go to log4j2.xml file in bin folder and uncomment the following

	1: <Logger name="org.apache.jmeter.protocol.http.control" level="debug" /> >>   responsible for logging events connected to the CookieManager, CacheManager, AuthManager and so on.
	2: <Logger name="org.apache.http" level="debug" /> >> will enable full wire and context logging >> Wire logging is logging of all data transferred between the server and JMeter when executing HTTP requests. 
		Use it only to debug problems, since storing all request and response data could take a lot of disk space.

	3: 


Installations on Remote Machine using Commands in GitBash:

Install latest java using yum commands

sudo su >> to get to the root folder

yum install java-1.8.0-openjdk >> to install latest java

For Jmeter Installation:

# from https://gist.github.com/smithbr/f2f19d7c362ef17530aaa7ccfaefeb06
#

# Download
curl http://mirror.ibcp.fr/pub/apache//jmeter/binaries/apache-jmeter-5.2.1.tgz > $HOME/apache-jmeter-5.2.1.tgz
tar -xvzf $HOME/apache-jmeter-5.2.1.tgz

# Create a .env file
echo "export JMETER_HOME=$HOME/apache-jmeter-5.2.1.tgz" > .jmeter.env
echo "export PATH=$PATH:$JMETER_HOME/bin" >> .jmeter.env
source .jmeter.env


========

How to run jmeter on Linux machine

>> ./jmeter -n -t shahid-test-plans/Fizz_cleanspeak.jmx -l shahid-test-plans/LinuxJTL.jtl


======

Commands to check hardware information on Linux:

>> lscpu > information about the cpu and processing units
>> lshw >  List Hardware
>> sudo fdisk -l > Fdisk is a utility to modify partitions on hard drives, and can be used to list out the partition information as well
>> free -m >> Check the amount of used, free and total amount of RAM on system

======

ulimit and its commands:

Command >> ulimit -a >> to print all the resoruce limits of a current user

core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 3860
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 3860
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited

>> ulimit --help
>> man limits.conf
>> sudo vim /etc/security/limits.conf >> to manually modify the ulimit values 
	>> Cntrl + z to exit the window
	>> i to start insert mode
	>> change the lines of code
	>> ESC to exit Insert mode
	>> :wq to save and exit the vim editor >> They have the following structure <domain> <type> <item> <value>
>> man limits.conf >> For the in-depth info on the “limits.conf” configuration file




All about swapfile

https://itsfoss.com/create-swap-file-linux/

1: Create a Swap file >> sudo fallocate -l 1G /swapfile 
2: To give read/write permissions to root user  >> sudo chmod 600 /swapfile
3: Mark the new file as swap space >> sudo mkswap /swapfile
	Output should be like this >> Setting up swapspace version 1, size = 1024 MiB (1073737728 bytes)
no label, UUID=7e1faacb-ea93-4c49-a53d-fb40f3ce016a
4: Enable the swap file>> sudo swapon /swapfile
5: To check the status of the swapspace >> swapon --show OR sudo swapon -s
	Output: like below 
	NAME       TYPE   SIZE USED PRIO
	/swapfile  file 1024M   0B   -2
6: To take the backup of the fstab file before editing it >> sudo cp /etc/fstab /etc/fstab.back
7: To make the swapfile usable even after reboot of linux system >> echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
	>> This will update the fstab file using command line
8: To adjust swappiness (default = 60) >> To check >> cat /proc/sys/vm/swappiness | to modify (soft) >> sudo sysctl vm.swappiness=25 
	To modify (hard) >> vm.swappiness=25
	(Swappiness: It determines how often the swap space should be used. The swappiness value ranges from 0 to 100)
9: To Resize swap space >> sudo swapoff /swapfile > sudo fallocate -l 2G /swapfile > sudo mkswap /swapfile > sudo swapon /swapfile
10: To remove swap file >> sudo swapoff /swapfile > sudo rm /swapfile

Vim editor in Linux:

>> vim filename
>> i for Insert mode
>> ESC to exit Insert mode and go to command mode
>> save: :w
>> save and exit: :wq
>> exit: :q
>> force: ! (example :w! :q!)

To change permissions of Directories:

>> sudo chown -R ec2-user:ec2-user apache-jmeter-5.2.1/ >> this will change ownership of directory to ec2-user (-R will change permissions to sub-directory level as well)

Removed all the listeners in test plan and its running on AWS instance

AWS instance size: RAM 1GB, ROM 8GB

Got the insufficient memory error for test plan with 	
	>> Users = 2000, Ramp Up = 20 and forever loop for 10 mins

Heap:
	heap is an area of pre-reserved computer main storage ( memory ) that a program process can use to store data in some variable amount that 
won't be known until the program is running. The process manages its allocated heap by requesting a "chunk" of the heap (called a heap block ) when needed, returning the blocks when no longer needed, 
and doing occasional "garbage collecting," which makes blocks available that are no longer being used and also reorganizes the available space in the heap so that it isn't being wasted in small unused pieces.

How to check the current allocated Heap size on your machine
	>> java -XX:+PrintFlagsFinal -version | grep HeapSize
		> Initial values on linux machine >> InitialHeapSize = 16777216 (16MB) >> MaxHeapSize =  260046848 (260MB)
	
	Updated the values using: >> The Java Virtual Machine takes two command line arguments which set the initial and maximum heap sizes
			> SET _JAVA_OPTIONS = -Xms512m -Xmx1024m (For windows)
			> export _JAVA_OPTIONS="-Xms1024m -Xmx2048m" (For Linux)
	To update the heap size permanently >> sudo vim /etc/profile and add >> export _JAVA_OPTIONS="-Xms1024m -Xmx2048m"
		To edit .bashrc and .bash_profile >> vim ~/.bashrc > vim ~/.bash_profile > export _JAVA_OPTIONS="-Xms1024m -Xmx2048m"

For Login shells, the config is read from these files:

/etc/profile (Always sourced)
$HOME/.bash_profile (the rest of these files are checked in order until one is found, then no others are read)
$HOME/.bash_login
$HOME/.profile

So, any of these files edited and added the heap size should work for permanent heap size change

Total memory usage equation is: 

(heap size) + (number of threads)x(thread stack size) = (total RAM used by JVM process).


