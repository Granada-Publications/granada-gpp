
#mode standard cpp

/* ======================
        Quran Related
   ======================*/

#define QREF #1, Q#2:#3

#define QURAN \
::: {custom-style="quran AR"}\
#1\
:::\
\
::: {custom-style="quran trans EN"}\
«#2»\
:::\
\
::: {custom-style="quran reference EN"}\
#3\
:::



/* ======================
        Ḥadīth Related
   ======================*/



/* ======================
        Honorifics
   ======================*/

#define SWT ([سبحانه وتعالى]{lang=ar})
#define PBUH ([صلى الله عليه وسلم]{lang=ar})
#define P_HIM ([رضي الله عنه]{lang=ar})
#define P_HER ([رضي الله عنها]{lang=ar})
#define P_TWO ([رضي الله عنهما]{lang=ar})
#define P_THM ([رضي الله عنهم]{lang=ar})
#define M_HIM ([رحمه الله تعالى]{lang=ar})

#define BSWT ([سبحانه وتعالى]{custom-style="kBody Honorifics"})
#define BPBUH ([صلى الله عليه وسلم]{custom-style="kBody Honorifics"})
#define BP_HIM ([رضي الله عنه]{custom-style="kBody Honorifics"})
#define BP_HER ([رضي الله عنها]{custom-style="kBody Honorifics"})
#define BP_TWO ([رضي الله عنهما]{custom-style="kBody Honorifics"})
#define BP_THM ([رضي الله عنهم]{custom-style="kBody Honorifics"})
#define M_HIM ([رحمه الله تعالى]{custom-style="kBody Honorifics"})

#define pyTime #exec python python/_pyTime.py

/* ==========================
        DOCUMENT METADATA
   ==========================*/

#include metadata.yaml

# Introduction

QURAN(
يَـٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُواْ ٱتَّقُواْ ٱللَّهَ حَقَّ تُقَاتِهِۦ وَلَا تَمُوتُنَّ إِلَّا وَأَنتُم مُّسۡلِمُونَ ١٠٢,
O you who believe! Fear Allāh (by doing all that He has ordered and by
abstaining from all that He has forbidden) as He should be feared. [Obey Him\, be
thankful to Him\, and remember Him always]\, and die not except in a state of
Islam [as Muslims (with complete submission to Allāh)].,
QREF(Āl ʿImrān,3,102))

## Tests

Hijri Date Output: pyTime

Output:   The Prophet PBUH  
Expected: The Prophet ([صلى الله عليه وسلم]{lang=ar})

Output:   Abū Bakr p(him)  
Expected: Abū Bakr (May Allāh be pleased with him)

Output:   Khadījah p(her)  
Expected: Khadījah (May Allāh be pleased with her)

Output:   QREF(al-Nisāʾ,4,111)  
Expected: al-Nisāʾ, Q4:111

The Prophet PBUH is reported to have said...

# TeX

#mode standard tex

\define{RADM}{([رضي الله عنه]{lang=ar})}

TeX: Abū Bakr \RADM

# HTML

\mode{standard}{html}

<#define RADF|([رضي الله عنها]{lang=ar})>

HTML: Khadījah <#RADF>

# XHTML

<#mode standard|xhtml>

<#define SWT|([سبحانه وتعالىٰ]{lang=ar})/>

XHTML: Allāh <#SWT/>
