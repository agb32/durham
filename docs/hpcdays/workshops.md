# Workshops

## Tuesday, 3rd June 2025

### Computational Biosciences
**Conveners: Christopher Marcotte (Durham) and Gokberk Kabacaoglu (Durham)**
- 9:30 - 10:30 and 11:00 - 12:30

Join us for 5 x 25-minute talks from the following speakers:
- Maria Secrier (University College London)
- Tyler Shendruk (University of Edinburgh)
- Ulrik Beierholm (Durham)
- More to be announced.


### DiRAC RSEs
**Convener: Ilektra Christidi (UCL)**
- 13:30 - 15:00 and 16:30 - 18:00

Join us for 4 x 20-minute talks, speakers to be confirmed.

This session is for the DiRAC RSEs to present their work to the UK HPC community, as well as catch up with each other and other DiRAC people that might want to join. Come join us to see how DiRAC RSEs accelerate science in particle physics, astrophysics, and cosmology, by promoting good software development practices, optimising software running on the DiRAC sites, and assisting researchers in implementing new functionality and using accelerators in their codes.

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

Organised by representatives from the Women in High Performance Computing (WHPC) community, this panel session will discuss where here EDI efforts in HPC are falling short and explore how we can rebalance the equation — together.

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

- Ben Went, Met Office:
   <details>
       <summary>"Using PSyclone, a domain specific compiler to parallelise the Met Office weather and Climate model with OpenMP"</summary>
      tbc
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

- Justs Zarins, EPCC:
   <details>
       <summary>"Exploring Dataflow Architectures for Improved Efficiency in Earth System Models"</summary>
     Earth system models are crucial for simulating environmental processes but demand significant computational resources and energy. In this presentation we will explore the potential of               dataflow architectures to enhance both computational and energy efficiency of ESMs. We will primarily discuss the Cerebras Wafer Scale Engine, examining its capabilities and evaluating                its suitability for the shallow water equation.
   </details>


### HPC/HTC in High-Energy Physics
**Conveners: Enrico Bothmann (CERN), Luigi del Debbio (Edinburgh), Marek Schoenherr (Durham)**
- 13:30 - 15:00

Speakers:
- Maria Girone (CERN)
- Dave Britton (Glasgow)
- Davide Constanzo (Sheffield)
- Manuel Griffels (KIT)


## Thursday, 5 June 2025

### eCSE Session
**Convener: Mladen Ivkovic (Durham University)**
- 9:45 - 10:30 and 11:00 - 12:30

The ARCHER2 GPU eCSE support provides funding to the UKRI research community to develop software in a sustainable manner to run on GPU-based architectures. Two such GPU eCSE calls have closed recently. In this knowledge exchange workshop, leads and developers of the funded projects present their current work and the challenges they're facing in their respective domains with regards to HPC GPU acceleration of scientific software.

Speakers:

- Chris Cantwell (Imperial College London)

  - Title: "Extending high-fidelity modelling with Nektar++ to the next generation of supercomputers"

  - Abstract: Nektar++ is a parallel and scalable C++ framework for the high-fidelity solution of partial differential equations using spectral/hp element methods. These methods provide a rich discretisation space, capable of efficiently and accurately capturing transient dynamics across a wide range of scales in highly complex geometries. The software is used in a wide range of application areas, including aeronautical, automotive and environmental engineering, the energy sector, and biomedicine. Initially developed nearly 20 years ago in a "CPU era", it has recently seen substantial development investment in transitioning the code to support heterogeneous technologies which form the basis of current and future HPC platforms. In this talk, I will share the key design decisions we have made, the algorithmic and implementation challenges we faced and our approach to addressing them, summarise our current performance on these modern platforms, and finally outline our vision for future developments.

- Jason McEven (UCL)

  - Title: Differentiable and Accelerated Spherical Transforms

  - Abstract: Many fields of science and engineering, in both academic and industrial settings, encounter data on spherical manifolds. The diversity of applications is quite remarkable, ranging from geophysics, exoplanets, and climate science, to early and late Universe cosmology, to biomedical imaging and molecular chemistry, and far beyond, such as gravitational waves and computer vision. While a number of codes are available to compute spherical harmonic transforms, for example, existing codes are not suitable for many modern scientific computing applications since they do not support automatic differentiation or GPU acceleration. We have developed the `s2x` suite of open-source spherical codes, with interfaces in both JAX and PyTorch, providing both automatic differentiation and GPU acceleration to facilitate differentiable programming workflows or AI models and to leverage the high-throughput of modern hardware accelerators. The suite includes [`s2fft`](https://github.com/astro-informatics/s2fft) for spherical harmonic transforms and Wigner transforms (Fourier transforms on the sphere and rotation group), [`s2wav`](https://github.com/astro-informatics/s2wav) for spherical wavelet transforms, [`s2scat`](https://github.com/astro-informatics/s2scat) for spherical scattering transforms (a powerful latent space for generative models), and [`s2ai`](https://github.com/astro-informatics/s2ai) for spherical AI models that exhibit excellent rotational equivariance properties. In this talk I will overview these codes and their underlying mathematical methods and computational algorithms. I will also touch briefly on the use of these codes for generative modelling of cosmological fields. We actively encourage new contributors for the `s2x` code suite and run [all-contributors](https://allcontributors.org/) to ensure all efforts are recognised -- don't hesitate to get in touch if you're interested or would just like to know more!

- Sebastien Lemaire (EPCC)

  - Title:  x3d2: a modern High Fidelity CFD Solver for CPU and GPU based supercomputers

  - Abstract: In an HPC environment where vendor specific development is needed to take full advantage of hardware, x3d2 -- an open-source, CFD solver based on high-order compact finite difference schemes and the successor to XCompact3d -- is designed with performance and hardware compatibility in mind targeting both GPU and CPUs.

    This talk will present the software architecture based on a Fortran object oriented approach allowing multiple implementations of low level backends to perform high level tasks as well as a novel data layout optimised to reduce cache misses and data movement for both CPU and GPU memory structures.

    The distributed tri-diagonal solver at the core of x3d2 showed to sustain 66% of the theoretical peak bandwidth at scale on both CPU and GPU based supercomputers.

- Nick Brown (EPCC)

- Phil Hasnip (University of York)

- Chris Johnson (EPCC)


### HPC/HTC in High-Energy Physics
**Conveners: Enrico Bothmann (CERN), Luigi del Debbio (Edinburgh), Marek Schoenherr (Durham)**
- 9:45 - 10:30

Speakers:
- Gurtej Kanwar (Edinburgh)
- Roy Stegman (Edinburgh)
- Antonin Portelli (Edinburgh)


### Benchmarking Symposium: Benchmarking of HPC systems for simulation and AI
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

We will invite speakers from across the benchmarking activities mentioned above and will also
actively seek presentations from other individuals and groups with relevant experience either
in the UK or internationally. We will also try to include at least one presentation by an
international partner to bring insights from outside the UK.


### HPC RSE SIG Meet-up
**Conveners: Marion Weinzierl, Nick Brown**
- 16:30 - 18:00

This is an in-person meet-up of the [HPC Research Software Engineers Special Interest Group (HPC RSE SIG)](https://society-rse.org/hpc-rse-sig/), but everyone is welcome -- you do not need to be involved with the SIG, the RSE Society, or even be an RSE!

We will start with an un-conference style discussion session (i.e., discussion topics and groups decided on by the participants), which will lead into further discussions and chats over beer and food in the evening.




## Friday, 6 June 2025

### Numerical Relativity
**Convener: Han Zhang**
- 9:45 - 10:30 and 11:00 - 12:30

More details coming soon!


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

We will invite speakers from across the benchmarking activities mentioned above and will also
actively seek presentations from other individuals and groups with relevant experience either
in the UK or internationally. We will also try to include at least one presentation by an
international partner to bring insights from outside the UK.


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

Organised by representatives from the Women in High Performance Computing (WHPC) community, this second session will bring the conversation to you! In the first part, taking place prior to this on Wednesday, we will host a panel discussion from representatives of the community to discuss getting the balance right as volunteers for EDI efforts in HPC. Don't worry, we will provide a complete summary, so please come along even if you missed the first session. This second session will be a group discussion, finding strategies to address these problems in the day-to-day, and advocate for small tangible changes.

Finally, in the third part of our session, Mike Simpson (Newcastle University) will lead a focused conversation on mental health around volunteering for EDI initatives. EDI work is often driven by deeply personal motivations, the emotional weight of this can take a toll and it's important to look after yourself. We want to help support you in this as well as advancing our community to improve the state of EDI.

### CoSeC
**Conveners: Stephen Longshaw (UKRI STFC), Damian Jones (UKRI STFC)**
- 13:30 - 15:00 (talks) and 15:30 - 16:30 (panel)

13:30 – 14:00 – Introducing CoSeC and the Collaborative Computational Community Model (Stephen Longshaw)

14:00 – 14:15 – Applied AI for the Digital Humanities (CCP-AHC; Karina Rodriguez Echavarria / Jeyan Thiyagalingam)

14:15 – 14:30 – Computational Biology (Martyn Winn – joining remotely)

14:30 – 14:45 – Computational Engineering (CCP-NTH, CCP-Turbulence, UKTC; Wei Wang)

14:45 – 15:00 – Computational Materials and Molecular Science (Marcello Puligheddu / Rajany RV)

**Panel: Creating a cohesive distributed Digital Research Infrastructure**

- Chair: Marion Weinzierl

- Panel: Katy Clough; Mark Wilkinson; Afia Masood; Nick Brown, Karina Rodriguez Echavarria, Tobias Weinzierl

 
The panel will kick off with a discussion of some key topics around a cohesive digital research infrastructure. After that, the audience will be given the opportunity to ask the panel further questions.
 
The basic idea is to discuss how (and whether?) it is possible for us to create a DRI using the distributed funding approach – i.e. funding the infrastructure as lots of smaller projects (relatively) that need to interoperate to be a single cohesive overall infrastructure.



### HPC/HTC in High-Energy Physics
**Convener: Enrico Bothmann (CERN), Luigi del Debbio (Edinburgh), Marek Schoenherr (Durham)**
- 13:30 - 15:00

Speakers:
- Daniel Maitre (Durham)
- Enrico Bothmann (CERN)
- Konrad Helms (Goettingen)
- Daniele Massaro (CERN)
