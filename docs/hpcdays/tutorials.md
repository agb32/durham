# Tutorials


## Monday, 2nd June 2025 

### ICCS: FTorch
**Presenters: Joe Wallwork, Tom Meltzer (ICCS, Cambridge)**
- 11:00 - 12:30

Fortran continues to be important to several scientific communities, such as weather and climate forecasting, plasma physics, and materials science.
Reasons for this include its natural support for mathematical operations on arrays, continued updates to the language standards and compilers, and considerable societal inertia.
However, Fortran lacks native support for machine learning (ML), for which popular tools such as PyTorch are written in Python.
There are several approaches to solve the language inter-operation problem to enable ML in Fortran (some of which discussed elsewhere in this workshop.)
The FTorch (https://github.com/Cambridge-ICCS/FTorch) approach makes use of the iso_c_binding intrinsic, facilitating the easy deployment of PyTorch-based models within Fortran codes by interfacing directly to the C++ Torch backend.
This approach avoids data copies and the need for a Python runtime, both of which can be problematic for HPC.

In this tutorial, attendees will:
- Write an ML model using PyTorch and load it for inference in Fortran using FTorch.
- Learn how to create, manipulate, and interrogate FTorch tensors.
- Experiment with FTorch's newly added automatic differentiation functionality.
- Hear about ongoing and future work on enabling online training.


### HPE: SmartSim
**Presenter: Alessandro Rigazzi (HPE), Holly Judge (HPE)**
- 13:30 - 15:00 - Session 1
- 15:00 - 15:30 - Coffee break 
- 15:30 - 17:00 - Session 2

As machine learning (ML) becomes more prevalent, it is unsurprising that using ML in combination with scientific HPC simulations has become more popular. Coupling HPC and ML in this way can improve the overall efficiency of HPC workflows by allowing ML predictions to help guide or replace parts of simulations.
However, there are challenges coupling the two approaches as HPC applications are typically written in C, C++ or Fortran and run on CPUs, whereas ML frameworks are usually Python based and benefit from being run on GPUs. In this tutorial we will introduce SmartSim, an open-source framework that has been developed to help address these challenges and allow researchers to easily adapt their traditional HPC workloads to include ML.  
 
In this two-part tutorial we will aim to familiarise the audience with SmartSim and demonstrate how it can be used to integrate ML into their own applications. In the first session we will give an overview of SmartSim and show it can interact with simulation data in HPC applications in order to integrate ML models. We will also show real examples of how SmartSim has been used in different fields of research such as Computational Fluid Dynamics and Climate Modelling. We also explain what needs to be done to integrate SmartSim into an application and to deploy the resulting workflow. 
 
The second session will take a more hands-on approach where attendees can run examples of hybrid scientific simulation/AI workflows using SmartSim.  Attendees will learn how to launch SmartSim leveraging the system’s native batch scheduler and job launcher and gain a practical understanding of the modifications required to adapt HPC applications to use ML.  
 
There would be an opportunity to discuss how users’ individual applications could be modified to use SmartSim. 


## Tuesday, 3rd June 2025 

### Lustre User Group: Darshan profiling on Lustre
**Presenters: Robert Esnouf, Alastair Basden**
- 09:00-10:00 - Talks
- 09:00-9:05 - Welcome
- 09:05-9:30 - Paul Ingram, Red Oak Consulting, Lustre PFL
- 09:30-9:55 - David Ford, Oxford, Tiering to tape
- 09:55-10:20 - Gwen Dawes, Filesystems for AI workloads: Linux and the IO Bottleneck
- 10:20-10:30 - Panel Q&A
- 10:30-11:00 - Coffee break
- 11:00-12:30 - Lustre discussion <s>Darshan introduction and tutorial - Rich Mansfield, DDN.</s>

[LUG Teams session](https://teams.microsoft.com/l/meetup-join/19%3ameeting_Mjc0YjlkMjEtMmQyYi00ZjlhLThmN2QtMjllNGY2YTRlMTcw%40thread.v2/0?context=%7b%22Tid%22%3a%227250d88b-4b68-4529-be44-d59a2d8a6f94%22%2c%22Oid%22%3a%22174fe4a1-ea76-4bc7-90e6-90976cc2117a%22%7d)


Learn about Lustre installations at various sites, and discuss your Lustre woes with experienced users.



### AMD GPUs: Simplify your HPC Application Port to GPUs - OpenMP and Managed Memory on AMD MI300A and MI300X
**Presenter: Bob Robey (AMD)**
- 09:00 - 10:30 - Session 1
- 10:30 - 11:00 - Coffee break
- 11:00 - 12:30 - Session 2

This will be a hands-on exploration of the new next-gen AMD Fortran and the C and C++ compiler implementation of the OpenMP offloading GPU compiler. We'll also exploit the managed memory capabilities of the APU Programming Model to make the porting much easier.

What kind of complex, real-world language constructs can these compilers handle? We look at many cases in C, C++, and Fortran. Bring your complex reproducers in Fortran and C++ and we'll see if we can break the compilers.


### Codeplay: Accelerate your code on GPUs and more using C++ and SYCL
**Presenter: Duncan McBain (Codeplay)**
- 13:30 - 15:00 - Session 1
- 15:00 - 16:30 - Coffee break & Opening Ceremony
- 16:30 - 18:00 - Session 2

Parallel programming can be used to take advantage of heterogeneous architectures including GPUs, FPGAs, XPUs, IPUs, TPUs or special units on CPUs to significantly increase the performance of applications. SYCL is an open standard programming model that is defined by the industry and lets developers support many of these processors from different vendors using a single code base and only modern standard C++ code.

This tutorial will give software developers the knowledge they need to begin developing parallel applications using C++ and the SYCL programming model. Our goal is to equip attendees with the skills they need to build highly performant applications that can be used in the fields of HPC and AI and deployed to multiple hardware platforms. We will cover the fundamentals of the SYCL programming model before moving to more advanced topics. We will explore how SYCL can be used to write serious applications, covering intermediate to advanced features of SYCL as well as some of the tools and libraries that support SYCL application development.
This is a hands-on tutorial, attendees will work through exercises that represent key design patterns encountered by people who program heterogeneous systems and deploy this code to multiple processors from different vendors.
