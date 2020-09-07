
#mode standard cpp
/* ======================
        Quran Related
   ======================*/

#mode standard tex
\define{\qref{surahName}{surahNumber}{ayahNumber}}{\surahName, Q\surahNumber:\ayahNumber}

\mode{standard}{cpp}
/* ======================
        Ḥadīth Related
   ======================*/

#mode standard cpp
/* ======================
        Honorifics
   ======================*/
#mode standard default

#define PBUH ([صلى الله عليه وسلم]{lang=ar})
#define pyTime #exec python python/_pyTime.py


#mode standard cpp
/* ==========================
        DOCUMENT METADATA
   ==========================*/
#include metadata.yaml

#mode standard default

# Introduction



## Tests

Output (\pyTime): pyTime

Output:   The Prophet PBUH  
Expected: The Prophet ([صلى الله عليه وسلم]{lang=ar})

Output:   Abū Bakr p(him)  
Expected: Abū Bakr (May Allāh be pleased with him)

Output:   Khadījah p(her)  
Expected: Khadījah (May Allāh be pleased with her)

Output:   qref(al-Nisāʾ,4,111)  
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
