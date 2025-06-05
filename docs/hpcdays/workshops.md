# Workshops

## Tuesday, 3rd June 2025

### Computational Biosciences
**Conveners: Christopher Marcotte (Durham) and Gokberk Kabacaoglu (Durham)**
- 9:30 - 10:30 and 11:00 - 12:30

Join us for 5 x 25-minute talks from the following speakers:
- Maria Secrier (University College London)
- Tyler Shendruk (University of Edinburgh)
- Ulrik Beierholm (Durham)
- Natalie Tatum (Newcastle University)
- Jonathon D. Liston (Durham)


### DiRAC RSEs
**Convener: Ilektra Christidi (UCL)**
- 13:30 - 15:00 and 16:30 - 18:00

This session is for the DiRAC RSEs to present their work to the UK HPC community, as well as catch up with each other and other DiRAC people that might want to join. Come join us to see how DiRAC RSEs accelerate science in particle physics, astrophysics, and cosmology, by promoting good software development practices, optimising software running on the DiRAC sites, and assisting researchers in implementing new functionality and using accelerators in their codes.

Agenda:
- Simon Burbidge (Leicester) & Ilektra Christidi (UCL) - 15 min
  - Intro: The DiRAC RSE team and what we can do for your research
- Nicolin Govender & Connor Aird (UCL) - 15 min
  - Evaluation of an implict stellar hydrodynamics code (Sparse Matrix) for GPU acceleration
- Muhammad Asif (Leicester) - 15 min
  - Optimising gauge calculations in GRID via the RAC16 call
- Julianna Kwan (Cambridge) - 15 min
  - AMRex for portability and its use in GRTeclyn
- Gokmen Kilic (DUrham) - 15 min
  - DiRAC RSE support for SWIFT
- Nicolin Govender (UCL) - 5 min
  - Parallel neighbour finding algorithm
- Simon Burbidge (Leicester) - 5 min
  - Thoughts about mixed precision
- Ilektra Christidi (UCL) - 5 min
  - Outro: Audience interaction & pairing with RSEs

**This workshop consists of two parts, and the second part (16:30 - 18:00) is for DiRAC RSEs only.**



## Wednesday, 4th June 2025

### Women in HPC (WHPC)
**Conveners: Eleanor Broadway (EPCC), Marion Weinzierl (ICCS)**
- 09:45 - 10:30

**The EDI Equation: Getting the Balance Wrong**

In order to drive change and impact around equality, diversity and inclusion (EDI) we need a finely tuned balance of:

* Passion: People who care deeply and take action
* Lived experience: Those who are directly affected to provide input
* Diversity of voices to ensure suitability for all
* Institutional buy-in: Support from leadership, feeding into career progression to incentivise engagement.
* Funding and resources
* Accountability and accurate reporting on success of initatives

But, when this balance tips the wrong way, we can see an unsustainable over-reliance on volunteer-driven initiatives with a lack of institutional buy-in and, ultimately, missed opportunities for driving real and impactful progress.

Organised by representatives from the Women in High Performance Computing (WHPC) community, this panel session will emphasise the importance of acknowledging the emotional toll and limitations of volunteer-led EDIA efforts, advocating for honest dialogue and a shift toward collective responsibility and practical strategies for redistributing the work. It also calls for a forward-looking approach centred on sustainable, inclusive change. Let's explore how we can rebalance the equation.

Our panelists are:

* Cristin Merritt, Alces Flight Ltd
* Jeremy Cohen, Imperial College London
* Selina Aragon, EPCC and the SSI
* Astrid Scott-Bennett, Research Computing Services, University of Cambridge

This workshop consists of two parts. The second, taking place on Friday, will be informed by and extend on this discussion.


### HPC in Weather & Climate Research
**Conveners: Chris Maynard (Met Office), Marion Weinzierl (ICCS, University of Cambridge)**
- 11:00 - 12:30 and 15:30 - 16:30

In this session we will hear from a series of speakers from the Weather and Climate Research community, talking about how they leverage HPC and AI in their domain.

Our speakers are:

- Greenville Lister, NCAS:
   <details>
       <summary>"The CANARI Large Ensemble climate modelling workflow."</summary>
      In tandem with technical developments in climate/Earth-System modelling, the vast majority of HPC resources is still consumed by running established models with relatively mature workflows on current platforms.
      We describe the CANARI HPC climate modelling workflow on ARCHER2 and JASMIN and discuss what it takes to run a modest climate modelling experiment.
   </details>

- Nell Hartney, University of Exeter:
   <details>
       <summary>"Incorporating an automatically differentiable dynamical core in training machine learning models for weather and climate."</summary>
      Machine learning (ML) approaches are becoming more and more widespread in weather and climate science. Applications range from emulating parametrisation schemes to data assimilation and more recently even to full ML-based weather and climate prediction models. The large quantities of data needed and the costly nature of training these ML models means that they are intrinsically linked with HPC.
      A common theme in ML-based schemes for weather and climate prediction is a significant deterioration in their performance at longer lead times due to rapidly growing errors and the model drifting outside the range of training data. One proposed solution for this issue is the idea of imposing physical constraints within the training loss function, which gives a tighter coupling at the training stage between this model physics and the data.
      The key ingredient in this approach is a differentiable physics-based model. Gusto, the dynamical core toolkit built on the Firedrake finite element library, is one such model that is automatically differentiable. Because full-scale weather and climate models are typically optimised for computational efficiency on specific computing hardware, scoping projects using the likes of Gusto are essential to provide guidance on decisions about HPC infrastructure.
      This talk will discuss our progress towards using Gusto as the differentiable dynamical core in a hybrid ML atmospheric model, in the style of NeuralGCM. We will investigate questions about the impact of the dynamical core formulation, including using a simplified equation set and different spatial and temporal discretisations.
   </details>

- Denis Sergeev, University of Exeter/ University of Bristol:
   <details>
       <summary>"Atmospheric dynamics on other planets"</summary>
      Detection and characterisation of exoplanetary atmospheres is entering a new era thanks to the new generation of powerful telescopes. To make the best use of observational data and guide future missions, we must advance our theoretical understanding of atmospheric dynamics. In this talk, I will show my recent work on adapting the Met Office's new 3D general circulation model (LFRic) to various exoplanets, from temperate terrestrial planets to hot Jupiters. I will talk about LFRic’s new capabilities and its potential for studying planetary atmospheres.
   </details>

- Joe Wallwork, ICCS, University of Cambridge:
   <details>
       <summary>"Accelerating UKCA by predicting timesteps with FTorch"</summary>
      The United Kingdom Chemistry and Aerosols (UKCA) model is a community atmospheric chemistry and aerosol microphysics model, which forms part of the Met Office's weather forecasting system. It is also a key part of the UK Earth System Model (UKESM), whose outputs feed into IPCC reports. UKCA is a particularly expensive part of the Met Office's model, so significant reductions to its computational cost would be welcome. The chemistry component of UKCA (the most expensive) uses an implicit timestepping scheme in which each iteration starts from a default, large timestep size. In each iteration, an attempt is made to solve the nonlinear system over several grid-boxes in the spatial domain, but in many cases this fails at the default timestep size. If so, the timestep size is repeatedly halved and the solver re-run until convergence is achieved. In this talk, we propose a method for predicting the timestep that will be required in advance,  thereby avoiding wasted computation in the attempts to run the chemistry model with timestep sizes that are too large. We utilise a simple machine learning (ML) based approach, coupled into UKCA using FTorch - a Fortran interface for the popular Python-based ML tool, PyTorch. Further, we make use of FTorch's recently added online training functionality, in order to avoid archiving training data that would have no clear other purpose.
   </details>

- Ben Went, Met Office:
   <details>
       <summary>"Using PSyclone, a domain specific compiler to parallelise the Met Office weather and Climate model with OpenMP"</summary>
      Momentum LFRic (A weather and Climate model developed by the MetOffice and partners) utilises an unstructured mesh and a tool named Psyclone, (a Domain Specific compiler for DSLs) to manage optimisations and communications across it’s code base.  LFRic also utilises existing code from the UM (The current Model), be it for physics, chemistry and aerosols, etc. However, existing optimisations in these codes are currently unaltered. Both codebases use differing data structures. LFRic uses a single dimension array, where the domain partition is grouped by levels, whereas UM codes using multidimensional arrays (following the pattern i, j, k). The change from a structured to an unstructured mesh in the model means that this structural difference can lead to occurrences where existing OpenMP optimisations present in UM source used by LFRic are no longer parallelising the work. PSyclone allows us to modify all loops in the existing files and update them. We can use OpenMP COLLAPSE to circumvent this issue, preserving existing optimisation intent and optimising for LFRic. Optimisations for GPU are also being explored (but not in this talk) which will also utilise PSyclone for modifying the source, maintaining consistent optimisation methods across the codebase which are also extensible.
   </details>

- Justs Zarins, EPCC:
   <details>
       <summary>"Exploring Dataflow Architectures for Improved Efficiency in Earth System Models"</summary>
     Earth system models are crucial for simulating environmental processes but demand significant computational resources and energy. In this presentation we will explore the potential of               dataflow architectures to enhance both computational and energy efficiency of ESMs. We will primarily discuss the Cerebras Wafer Scale Engine, examining its capabilities and evaluating                its suitability for the shallow water equation.
   </details>


### HPC/HTC in High-Energy Physics
**Conveners: Enrico Bothmann (CERN), Luigi del Debbio (Edinburgh), Marek Schoenherr (Durham)**
- 13:30 - 15:00
  This session focusses on developments for the Worldwide LHC Computing Grid (WLCG), its prospects and challenges.

Speakers:
- 13:30 Manuel Giffels (KIT)
   <details>
       <summary>"Transforming HEP Computing in Germany -- Paving the way for the efficient utilisation of HPC systems"</summary>
     Germany is undergoing a significant transformation in the landscape of High Energy Physics (HEP) computing. This presentation outlines the strategic migration of WLCG Tier-2 compute resources from dedicated university-based infrastructures to the National High-Performance Computing (NHR) centres. A cornerstone of this transition is the COBalD/TARDIS framework, which enables dynamic resource provisioning and facilitates seamless integration of heterogeneous HPC systems into the WLCG. Following a brief introduction to the Worldwide LHC Computing Grid (WLCG), with a particular emphasis on its structure and role within Germany, the presentation will explore the architecture and progress of the ongoing migration, share practical insights from experiences, and outline future directions.
   </details>
- 13:52 Dave Britton (Glasgow)
   <details>
       <summary>WLCG Overview</summary>
   </details>
- 14:15 Maria Girone / David Southwick (CERN)
   <details>
       <summary>HPC for WLCG</summary>
   </details>
- 14:37 Davide Constanzo (Sheffield)
   <details>
       <summary>Software for WLCG</summary>
   </details>


## Thursday, 5 June 2025

### eCSE Session
**Convener: Mladen Ivkovic (Durham University)**
- 9:45 - 10:30 and 11:00 - 12:30

The ARCHER2 GPU eCSE support provides funding to the UKRI research community to develop software in a sustainable manner to run on GPU-based architectures. Two such GPU eCSE calls have closed recently. In this knowledge exchange workshop, leads and developers of the funded projects present their current work and the challenges they're facing in their respective domains with regards to HPC GPU acceleration of scientific software.

Speakers:

- Chris Johnson (EPCC)

  - *Title*: EPCC eCSE Software Development Programmes

  - *Abstract*: Since the beginning of the ARCHER service in 2013 and continuing throughout the ARCHER2 service, EPCC has run an eCSE (embedded Computational Science and Engineering) software development programme, so far awarding around 190 projects a total of around 2100 person months of effort (175 staff years!). The initial calls were focussed mainly on the hardware of ARCHER and ARCHER2 meaning that most of the development was CPU based. More recently we opened 2 highly popular calls for GPU-based software development. As an introduction to the talks which follow, which will describe specific eCSE projects from the recent GPU calls, I will describe the evolution of the eCSE programme and some of the highlights.

- Jason McEven (UCL)

  - *Title*: Differentiable and Accelerated Spherical Transforms

  - *Abstract*: Many fields of science and engineering, in both academic and industrial settings, encounter data on spherical manifolds. The diversity of applications is quite remarkable, ranging from geophysics, exoplanets, and climate science, to early and late Universe cosmology, to biomedical imaging and molecular chemistry, and far beyond, such as gravitational waves and computer vision. While a number of codes are available to compute spherical harmonic transforms, for example, existing codes are not suitable for many modern scientific computing applications since they do not support automatic differentiation or GPU acceleration. We have developed the `s2x` suite of open-source spherical codes, with interfaces in both JAX and PyTorch, providing both automatic differentiation and GPU acceleration to facilitate differentiable programming workflows or AI models and to leverage the high-throughput of modern hardware accelerators. The suite includes [`s2fft`](https://github.com/astro-informatics/s2fft) for spherical harmonic transforms and Wigner transforms (Fourier transforms on the sphere and rotation group), [`s2wav`](https://github.com/astro-informatics/s2wav) for spherical wavelet transforms, [`s2scat`](https://github.com/astro-informatics/s2scat) for spherical scattering transforms (a powerful latent space for generative models), and [`s2ai`](https://github.com/astro-informatics/s2ai) for spherical AI models that exhibit excellent rotational equivariance properties. In this talk I will overview these codes and their underlying mathematical methods and computational algorithms. I will also touch briefly on the use of these codes for generative modelling of cosmological fields. We actively encourage new contributors for the `s2x` code suite and run [all-contributors](https://allcontributors.org/) to ensure all efforts are recognised -- don't hesitate to get in touch if you're interested or would just like to know more!

- Nick Brown (EPCC)

- Chris Cantwell (Imperial College London)

  - *Title*: Extending high-fidelity modelling with Nektar++ to the next generation of supercomputers

  - *Abstract*: Nektar++ is a parallel and scalable C++ framework for the high-fidelity solution of partial differential equations using spectral/hp element methods. These methods provide a rich discretisation space, capable of efficiently and accurately capturing transient dynamics across a wide range of scales in highly complex geometries. The software is used in a wide range of application areas, including aeronautical, automotive and environmental engineering, the energy sector, and biomedicine. Initially developed nearly 20 years ago in a "CPU era", it has recently seen substantial development investment in transitioning the code to support heterogeneous technologies which form the basis of current and future HPC platforms. In this talk, I will share the key design decisions we have made, the algorithmic and implementation challenges we faced and our approach to addressing them, summarise our current performance on these modern platforms, and finally outline our vision for future developments.


- Sebastien Lemaire (EPCC)

  - *Title*:  x3d2: a modern High Fidelity CFD Solver for CPU and GPU based supercomputers

  - *Abstract*: In an HPC environment where vendor specific development is needed to take full advantage of hardware, x3d2 -- an open-source, CFD solver based on high-order compact finite difference schemes and the successor to XCompact3d -- is designed with performance and hardware compatibility in mind targeting both GPU and CPUs.

    This talk will present the software architecture based on a Fortran object oriented approach allowing multiple implementations of low level backends to perform high level tasks as well as a novel data layout optimised to reduce cache misses and data movement for both CPU and GPU memory structures.

    The distributed tri-diagonal solver at the core of x3d2 showed to sustain 66% of the theoretical peak bandwidth at scale on both CPU and GPU based supercomputers.

- Phil Hasnip (University of York)

  - *Title*: Materials modelling, GPUs and the CASTEP code: Does accelerated computing lead to accelerated science?

  - *Abstract*: CASTEP is a materials modelling program based on quantum mechanics, which is capable of predicting physical, chemical and electronic properties of materials. It has been developed over more than two decades, and is used widely around the world, not only in academia but also in industry, via its inclusion in Dassault Systemes' Materials Studio product.

    Over the last few years, we have been developing and optimising a GPU-capable version CASTEP. I will discuss the challenges and successes in taking CASTEP's large Fortran+OpenMP+MPI codebase and adapting it to exploit GPUs, including recent successes from the PAX-HPC ExCALIBUR project and the plan for the new GPU-eCSE project.



### HPC/HTC in High-Energy Physics
**Conveners: Enrico Bothmann (CERN), Luigi del Debbio (Edinburgh), Marek Schoenherr (Durham)**
- 9:45 - 10:30
  This session focusses on the use of HPC and generative AI technologies
  for lattice QCD calculations

Speakers:
- 09:45 Gurtej Kanwar (Edinburgh)
   <details>
       <summary>"Generative AI for Lattice QCD calculations"</summary>
       Lattice QCD calculations provide valuable ab-initio inputs to study the Standard Model of particle physics. While Lattice QCD has made tremendous progress via large-scale Monte Carlo simulations, improved simulation resolutions are needed to access new quantities and further control systematic errors. I will summarize ongoing efforts to apply generative AI methods to solve this bottleneck, with particular emphasis on the computational challenges and opportunities of the generative AI approach.
   </details>

- 10:00 Roy Stegeman (Edinburgh)
   <details>
       <summary>"Determining the structure of the proton with Machine Learning"</summary>
       Predictions at proton colliders such as the LHC require an accurate and precise knowledge of the structure of the colliding protons in terms of their constituent quarks and gluons. In this talk We will review the methodology used by NNPDF collaboration to solve the inverse problem of extracting the parton distribution functions from a finite set of data, along with an estimate of their uncertainty, and the opportunities provided by deploying these fits on GPUs.
   </details>

- 10:15 Antonin Portelli (Edinburgh)
   <details>
       <summary>"Physics-focused system design"</summary>
       In this talk, we present the physics-focused approach taken by the STFC DiRAC facility to design the Tursa supercomputer. I will summarise how lattice QCD benchmarks, based on the Grid library, were used during the procurement process as well as for optimising system energy efficiency in production. This approach enabled Tursa to deliver scientific results from the first days of its production cycle and can be extended across research fields in the future.
   </details>


## Benchmarking Symposium: Benchmarking of HPC systems for simulation and AI
**Conveners: DiRAC, ExCALIBUR, UKRI Living Benchmarks**
**Lead: Mark Wilkinson**
- 16:30 - 18:00

Benchmarking is an essential part of the co-design and procurement of large-scale computing
systems, supporting the deployment of cost-e8ective, productive services. Benchmarks are
also valuable tools for obtaining quantitative information about the health of systems following
their deployment in production, for example confirming that application performance is
maintained following system software updates.

The UK has an outstanding track record of the successful use of science benchmarks to
optimise the design of large-scale computing services. There are a number of recent and
currently active projects in this area, including the ExCALIBUR Benchmarking project, the
ExCALIBUR BASE-II project, the UKRI Living Benchmarks project and the DiRAC-4 design
process. As UKRI develops its plans for the services which will comprise the future DRI
ecosystem, a workshop to discuss the benefits and challenges of e8ective benchmarking is
particularly timely.

The goals of this workshop are to:

1. share experiences (both positive and negative) and tools related to the development and
application of benchmark codes in system co-design, procurement or health-checking.
2. support the development and sharing of best practice in the area of benchmarking


**16:30 Garth Wells** (Cambridge) - "The UKRI Living Benchmarks Project"

**16:50 Jeyan Thiyagalingam** (STFC SciML group) – "AI benchmarks" 

**17:05 Mark Wilkinson** (DiRAC, Leicester) – "DiRAC co-design and benchmarking" 

**17:20 Panel discussion**

**18:00 End**


### HPC RSE SIG Meet-up
**Conveners: Marion Weinzierl, Nick Brown**
- 16:30 - 18:00

This is an in-person meet-up of the [HPC Research Software Engineers Special Interest Group (HPC RSE SIG)](https://society-rse.org/hpc-rse-sig/), but everyone is welcome -- you do not need to be involved with the SIG, the RSE Society, or even be an RSE!

We will start with an un-conference style discussion session (i.e., discussion topics and groups decided on by the participants), which will lead into further discussions and chats over beer and food in the evening.




## Friday, 6 June 2025

### Numerical Relativity
**Convener: Han Zhang**

Numerical relativity stands as a powerful tool for understanding astrophysical phenomena in strong-gravity regions. Solving the full non-linear Einstein equations numerically is notoriously computationally expensive, necessitating advanced high-performance computing techniques to accelerate simulations. In this workshop, we have invited researchers and experts in the field to share their experiences implementing HPC solutions for these complex evolving systems. Speakers will discuss both the computational challenges they've overcome and the exciting scientific discoveries enabled by their simulations, providing a comprehensive view of how cutting-edge HPC approaches are advancing our understanding of relativistic astrophysics.

*9:45 - 10:30*

- Robyn Munoz (University of Sussex)

  - *Title*: Introduction to Einstein Toolkit
  - *Abstract*: Einstein Toolkit is an open-source collection of interdependent codes designed to simulate and analyse relativistic scenarios involving black holes, neutron stars, cosmological structures and much more. With its modular design and broad applicability, this code exemplifies how physicists turn equations into simulations and run them on computing clusters.

- Shaun Swain (University of Birmingham)

  - *Title*: Strong-Field Scattering of Black Holes
  - *Abstract*: To detect and analyse gravitational wave signals from compact binaries requires extremely accurate theoretical models. Current state-of-the-art models blend analytical calculations with predictions arising from numerical relativity simulations, providing insight into the strong-field behaviour of gravitational interactions. Newly discovered relationships between quantum scattering amplitudes and classical observables in general relativity are providing novel tools to generate high-order analytical calculations. In this talk, I will demonstrate the critical role played by numerical relativity simulations in validating these calculations and allowing us to explore gravitational interactions at high-energies, where current theoretical predictions break down.

*11:00 - 12:30*

- Miguel Bezares Figueroa (University of Nottingham)

  - *Title*: MHDuet: Modelling General Relativistic MHD on  CPU/GPU Architectures
  - *Abstract*: MHDuet is an automatically generated, efficient computational code designed to simulate the dynamics of strongly gravitating, high-density matter in astrophysical scenarios involving compact objects such as black holes and neutron stars. Although MHDuet was initially developed on the SAMRAI infrastructure, which provides support for distributed adaptive mesh refinement (AMR), it is currently being ported to AMReX to exploit the capabilities of modern GPU-accelerated and massively parallel systems. The code solves the equations of general relativistic magnetohydrodynamics (GRMHD) and incorporates recent features aimed at improving accuracy and performance. I will provide an overview of the physical systems MHDuet can evolve and highlight the latest developments in its HPC capabilities.

- Alice Bonino (University of Birmingham)

  - *Title*: Improving eccentric gravitational waveform models with Numerical Relativity
  - *Abstract*: The formation and evolutionary pathways of stellar-mass binary black holes remains an unresolved question that can be addressed by precise measurements of the binary and orbital parameters from their gravitational-wave signal. Such binaries are expected to circularize due to the emission of gravitational waves as they approach merger. However, depending on their formation channel, some binaries could retain a non-negligible eccentricity when entering the frequency band of current gravitational-wave detectors. In order to meaningfully measure the eccentricity in an observed gravitational-wave signal, reliable waveform models that describe binaries on eccentric orbits are necessary. In recent years, significant effort has been invested in incorporating eccentricity into the current generation of waveform models using different analytical techniques such as post-Newtonian theory, gravitational self force and scattering paradigms. However, whilst these provide an accurate description of the gravitational-wave signals throughout the inspiral, they are only valid up to moderate eccentricities and are not reliable as the binary approaches merger.  To mitigate against such limitations, one can appeal to Numerical Relativity simulations to help model the complete inspiral-merger-ringdown signal from eccentric binaries. In this talk I will present methods for comparing Numerical Relativity simulations with waveform models for coalescing binary black holes developed within the Effective-One-Body framework. 

- Timothy Stokes (Durham University)

  - *Title*: Automated Kernel Generation for the Numerical Relativity Solver ExaGRyPE
  - *Abstract*: ExaHyPE is a numerical engine used to solve hyperbolic PDE systems, with a variety of use-cases. To handle these different cases, we require a suite of available numerical schemes to choose from, each of which requiring a large time investment into development and optimisation. The specific optimisation approach also depends on the application and type of hardware used, which cannot be fully predicted at the time that the scheme is developed. As a result many kernel variants must be maintained, including variants for different GPU offloading strategies. This talk details the status of the ExaHyPe-DSL eCSE project which replaces these manual kernels with those written using a Domain Specific Language (DSL).
The use of a DSL means that the code written is conceptually similar to the target problem and is abstracted away from any optimisation decisions. We have developed a Python based DSL which then generates optimised kernels using the ExCALIBUR xDSL toolkit. This allows for scientists to spend their time studying novel physics, instead of maintaining code. We focus on its application in the ExaGRyPE project, a numerical relativity solver developed on top of ExaHyPE.

### Benchmarking Symposium: Benchmarking of HPC systems for simulation and AI
**Conveners: DiRAC, ExCALIBUR, UKRI Living Benchmarks**
**Lead: Mark Wilkinson**

- 9:45 - 10:30

Benchmarking is an essential part of the co-design and procurement of large-scale computing
systems, supporting the deployment of cost-e8ective, productive services. Benchmarks are
also valuable tools for obtaining quantitative information about the health of systems following
their deployment in production, for example confirming that application performance is
maintained following system software updates.

The UK has an outstanding track record of the successful use of science benchmarks to
optimise the design of large-scale computing services. There are a number of recent and
currently active projects in this area, including the ExCALIBUR Benchmarking project, the
ExCALIBUR BASE-II project, the UKRI Living Benchmarks project and the DiRAC-4 design
process. As UKRI develops its plans for the services which will comprise the future DRI
ecosystem, a workshop to discuss the benefits and challenges of e8ective benchmarking is
particularly timely.

The goals of this workshop are to:

1. share experiences (both positive and negative) and tools related to the development and
application of benchmark codes in system co-design, procurement or health-checking.
2. support the development and sharing of best practice in the area of benchmarking

**09:45-10:00 Tuomas Koskela** (UCL) - "The Reframe framework"

**10:00-10:15 Adam Tuft** (Durham) - "Performance Modelling of Detrimental Task Execution Patterns in Mainstream OpenMP Runtimes" 

**10:15-10:30 Panel discussion** (continued)

**10:30** End


### Women in HPC (WHPC)
**Conveners: Eleanor Broadway (EPCC), Marion Weinzierl (ICCS)**
- 11:00 - 12:30

**The EDI Equation: Getting the Balance Wrong**

In order to drive change and impact around equality, diversity and inclusion (EDI) we need a finely tuned balance of:

* Passion: People who care deeply and take action
* Lived experience: Those who are directly affected to provide input
* Diversity of voices to ensure suitability for all
* Institutional buy-in: Support from leadership, feeding into career progression to incentivise engagement.
* Funding and resources
* Accountability and accurate reporting on success of initatives

But, when this balance tips the wrong way, we can see an unsustainable over-reliance on volunteer-driven initiatives with a lack of institutional buy-in and, ultimately, missed opportunities for driving real and impactful progress.

Organised by representatives from the Women in High Performance Computing (WHPC) community, this panel session will emphasise the importance of acknowledging the emotional toll and limitations of volunteer-led EDIA efforts, advocating for honest dialogue and a shift toward collective responsibility and practical strategies for redistributing the work. It also calls for a forward-looking approach centred on sustainable, inclusive change. Don't worry, we will provide a complete summary, so please come along even if you missed the first session. This second session will be a group discussion, we want to hear your opinions on this issue and work together to find sustainable solutions.

Finally, in the third part of our session, Mike Simpson (Newcastle University) will lead a focused conversation on mental health around volunteering for EDI initiatives. EDI work is often driven by deeply personal motivations, the emotional weight of this can take a toll and it's important to look after yourself. We want to help support you in this as well as advancing our community to improve the state of EDI.

### CoSeC & Creating a cohesive distributed Digital Research Infrastructure

**Conveners: Stephen Longshaw (UKRI STFC), Damian Jones (UKRI STFC)**
- 13:30 - 15:00 and 15:30 - 17:00

**Talks**

- 13:30 – 14:00 – Introducing CoSeC and the Collaborative Computational Community Model (Stephen Longshaw)
- 14:00 – 14:15 – Applied AI for the Digital Humanities (CCP-AHC; Karina Rodriguez Echavarria)
- 14:15 – 14:30 – Computational Biology (Martyn Winn – joining remotely)
- 14:30 – 14:45 – Computational Engineering (CCP-NTH, CCP-Turbulence, UKTC; Wei Wang)
- 14:45 – 15:00 – Computational Materials and Molecular Science (Marcello Puligheddu / Rajany RV)

**Panel: Creating a cohesive distributed Digital Research Infrastructure**

Chair: Marion Weinzierl

Panel: Katy Clough; Mark Wilkinson; Afia Masood; Nick Brown, Stephen Longshaw, Tobias Weinzierl, Karina Rodriguez Echavarria

The panel will kick off with a discussion of some key topics around a cohesive digital research infrastructure. After that, the audience will be given the opportunity to ask the panel further questions.

### HPC/HTC in High-Energy Physics
**Convener: Enrico Bothmann (CERN), Luigi del Debbio (Edinburgh), Marek Schoenherr (Durham)**
- 13:30 - 15:00
  This session focusses on the use of machine learning technoligies and GPU
  off-loading in Monte-Carlo event generation and simulation.

Speakers:
- 13:30 Daniel Maitre (Durham)
   <details>
       <summary>"Neural Networks for Matrix Element emulation"</summary>
   </details>

- 13:52 Konrad Helms (Goettingen)
   <details>
       <summary>"From Code to Collisions: Machine Learning-Driven Phase Space Sampling for Event Generation in High-Energy Physics"</summary>
       As we advance toward the next generation of particle collision experiments, there is a growing need for faster and more resource-friendly simulation of collision events in particle physics. This presentation highlights one of the main challenges in event generation: the integration of the transition matrix element. Many common software libraries currently utilize Monte Carlo integration techniques for this purpose. Recent progress in generative models in the form of continuous normalizing flows, trained using conditional flow matching, offers the potential to improve integration efficiency significantly. This presentation will demonstrate the application of continuous normalizing flows in neural importance sampling and discuss strategies for efficiently integrating functions with recursive structures.
   </details>

- 14:15 Enrico Bothmann (CERN)
   <details>
       <summary>"Portable collider event generation with PEPPER 🌶️"</summary>
       Collision simulations at high energies using Monte-Carlo event generators are a backbone of the physics programme of current and future particle physics experiments at the High Energy Frontier. The computational cost of these simulations is significant, and it will increase dramatically for the upcoming "High-Luminosity" update of the Large Hadron Collider at CERN. It is therefore desirable to be able to offload Monte-Carlo event generation to HPC facilities which increasingly rely on GPU acceleration. In this talk I present PEPPER, a new portable parton-level event generator with HPC and GPU support. It can be run on a variety of CPU and GPU architectures of today’s rapidly changing HPC landscape, and delivers 1-2 orders of magnitude faster event generation throughput for the computationally most relevant physics processes.
   </details>

- 14:37 Daniele Massaro (CERN)
   <details>
       <summary>"Data parallelism in MadGraph: hardware acceleration with GPUs and SIMD CPUs"</summary>
       The MadGraph5_aMC@NLO generator is a widely used tool for simulating high-energy particle collisions, and it is a key component of the LHC experiments' software stack. Recently, a new plugin of the code, CUDACPP, has been released along with the latest version of the code. The CUDACPP plugin represents the first endeavour on the path to hardware-accelerated event generation, opening MadGraph5_aMC@NLO to the world of GPUs and vector CPU instructions. Achieving this goal required the design of a new architecture of the code, and several steps of test and validation across many physics processes. At the same time, many tests have been carried out on the experimental side, providing feedback on the performance of the code and its usability. In this talk, we will start from presenting the original status of the code, detailing the main bottlenecks and the main strategies used to tackle them. Additionally, the main design choices will be introduced, followed by the results of performance and profiling tests. We will conclude with a discussion on the future developments and improvements that are planned for the next releases of the code, involving mainly the support of next-to-leading-order processes.
   </details>
