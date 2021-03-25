
#mode standard cpp
/* ======================
        Quran Related
   ======================*/
#mode standard tex

\define{\qref{surahName}{surahNumber}{ayahNumber}}{\surahName, Q\surahNumber:\ayahNumber}

\define{\quran{arabic}{translation}{reference}}{
::: {custom-style="Quran Arabic" dir="rtl"}
\arabic
:::

::: {custom-style="Quran Translation"}
«\translation »
:::

::: {custom-style="Quran Reference"}
\reference
:::
}

\mode{standard}{cpp}
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


## Tests

Hijri Date Output: pyTime

Output:   The Prophet PBUH  
Expected: The Prophet ([صلى الله عليه وسلم]{lang=ar})

Output:   Abū Bakr P_HIM  
Expected: Abū Bakr (May Allāh be pleased with him)

Output:   Khadījah P_HER  
Expected: Khadījah (May Allāh be pleased with her)

#mode standard tex
Output:   \qref{al-Nisāʾ}{4}{111}  
Expected: al-Nisāʾ, Q4:111

\quran{
وَكَمۡ أَهۡلَكۡنَا مِن قَرۡيَةِۢ بَطِرَتۡ مَعِيشَتَهَاۖ فَتِلۡكَ مَسَٰكِنُهُمۡ لَمۡ تُسۡكَن مِّنۢ بَعۡدِهِمۡ إِلَّا قَلِيلٗاۖ وَكُنَّا نَحۡنُ ٱلۡوَٰرِثِينَ ٥٨
}{And how many a town (population) have We destroyed, which was thankless for its
means of livelihood (disobeyed Allah, and His Messengers, by doing evil deeds
and crimes)! And those are their dwellings, which have not been inhabited after
them except a little. And verily, We have been the inheritor.}{\qref{al-Qaṣaṣ}{28}{58}}

\mode{standard}{cpp}

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
