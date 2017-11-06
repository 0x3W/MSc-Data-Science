/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * @author Dovla
 *
 */
// import libraries
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.ScoreDoc;

import java.io.*;
import java.util.Scanner;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.document.IntField;
import org.apache.lucene.document.LongField;
import org.apache.lucene.document.TextField;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.RAMDirectory;
import static org.apache.lucene.util.Version.LUCENE_41;

// initiate abstract class Animal
    public abstract class Animal {
// set variables
        public int age;
        public String name; 
        public String desc;
// create a method for passing variables
        public Animal(int age, String name, String desc)
        {
            this.age = age;
            this.name = name;
            this.desc = desc;

        }
// create a method for feedMe
        public abstract String feedMe(String food);
// initiate main
        public static void main(String[] args) throws IOException, ParseException {
// initiate array to store 14 Animals properties   
        Animal[] anims;
        anims = new Animal[14];
// populate array with Animals properties   

        anims[0] = new Herbivores(1,"Elephants","Elephants are large mammals of the family Elephantidae and the order Proboscidea. Three species are currently recognized: the African bush elephant (Loxodonta africana), the African forest elephant (L. cyclotis), and the Asian elephant (Elephas maximus). Elephants are scattered throughout sub-Saharan Africa, South Asia, and Southeast Asia. Elephantidae is the only surviving family of the order Proboscidea; other, now extinct, members of the order include deinotheres, gomphotheres, mammoths, and mastodons.");
        anims[1] = new Herbivores(2,"Rabbits","Rabbits are small mammals in the family Leporidae of the order Lagomorpha, found in several parts of the world. There are eight different genera in the family classified as rabbits, including the European rabbit (Oryctolagus cuniculus), cottontail rabbits (genus Sylvilagus; 13 species), and the Amami rabbit (Pentalagus furnessi, an endangered species on Amami Ōshima, Japan). There are many other species of rabbit, and these, along with pikas and hares, make up the order Lagomorpha. The male is called a buck and the female is a doe; a young rabbit is a kitten or kit.");
        anims[2] = new Herbivores(3,"Manatees","Manatees (family Trichechidae, genus Trichechus) are large, fully aquatic, mostly herbivorous marine mammals sometimes known as sea cows. There are three accepted living species of Trichechidae, representing three of the four living species in the order Sirenia: the Amazonian manatee (Trichechus inunguis), the West Indian manatee (Trichechus manatus), and the West African manatee (Trichechus senegalensis). They measure up to 4.0 metres (13.1 ft) long, weigh as much as 590 kilograms (1,300 lb),[1] and have paddle-like flippers. The etymology of the name is dubious, with connections having been made to Latin \"manus\" (hand), and to a word sometimes cited as \"manati\" used by the Taíno, a pre-Columbian people of the Caribbean, meaning \"breast\".[2] Manatees are occasionally called sea cows, as they are slow plant-eaters, peaceful and similar to cows on land. They often graze on water plants in tropical seas.");
        anims[3] = new Herbivores(4,"Deer","Deer (singular and plural) are the ruminant mammals forming the family Cervidae. The two main groups are the Cervinae, including the muntjac, the fallow deer and the chital, and the Capreolinae, including the elk, reindeer (caribou), the Western roe deer, and the moose. Female reindeer, and male deer of all species (except the Chinese water deer), grow and shed new antlers each year. In this they differ from permanently horned antelope, which are in the same order, Artiodactyla.");
        
        anims[4] = new Omnivores(5,"Humans","Modern humans (Homo sapiens, primarily ssp. Homo sapiens sapiens) are the only extant members of the subtribe Hominina, a branch of the tribe Hominini belonging to the family of great apes. They are characterized by erect posture and bipedal locomotion; high manual dexterity and heavy tool use compared to other animals; and a general trend toward larger, more complex brains and societies.[3][4]");
        anims[5] = new Omnivores(6,"Bears","Bears are carnivoran mammals of the family Ursidae. They are classified as caniforms, or doglike carnivorans. Although only eight species of bears are extant, they are widespread, appearing in a wide variety of habitats throughout the Northern Hemisphere and partially in the Southern Hemisphere. Bears are found on the continents of North America, South America, Europe, and Asia. Common characteristics of modern bears include large bodies with stocky legs, long snouts, small rounded ears, shaggy hair, plantigrade paws with five nonretractile claws, and short tails.");
        anims[6] = new Omnivores(7,"Lemurs","Lemurs (/ˈliːmər/ (About this sound listen) LEE-mər) are a clade of strepsirrhine primates endemic to the island of Madagascar. The word lemur derives from the word lemures (ghosts or spirits) from Roman mythology and was first used to describe a slender loris due to its nocturnal habits and slow pace, but was later applied to the primates on Madagascar. As with other strepsirrhine primates, such as lorises, pottos, and galagos (bush babies), lemurs share resemblance with basal primates. In this regard, lemurs are often confused with ancestral primates, when in actuality, lemurs did not give rise to monkeys and apes, but evolved independently.[5]");
        anims[7] = new Omnivores(8,"Raccoons","The raccoon (/rəˈkuːn/ or US: /ræˈkuːn/ (About this sound listen), Procyon lotor), sometimes spelled racoon,[3] also known as the common raccoon,[4] North American raccoon,[5] northern raccoon[6] and colloquially as coon,[7] is a medium-sized mammal native to North America. The raccoon is the largest of the procyonid family, having a body length of 40 to 70 cm (16 to 28 in) and a body weight of 3.5 to 9 kg (8 to 20 lb). Its grayish coat mostly consists of dense underfur which insulates it against cold weather. Two of the raccoon's most distinctive features are its extremely dexterous front paws and its facial mask, which are themes in the mythologies of the indigenous peoples of the Americas. Raccoons are noted for their intelligence, with studies showing that they are able to remember the solution to tasks for up to three years.[8] The diet of the omnivorous raccoon, which is usually nocturnal, consists of about 40% invertebrates, 33% plant foods, and 27% vertebrates.");
        anims[8] = new Omnivores(9,"Birds","Birds (Aves) are a group of endothermic vertebrates, characterised by feathers, toothless beaked jaws, the laying of hard-shelled eggs, a high metabolic rate, a four-chambered heart, and a strong yet lightweight skeleton. Birds live worldwide and range in size from the 5 cm (2 in) bee hummingbird to the 2.75 m (9 ft) ostrich. They rank as the class of tetrapods with the most living species, at approximately ten thousand, with more than half of these being passerines, sometimes known as perching birds. Birds are the closest living relatives of crocodilians. Birds are descendants of extinct dinosaurs with feathers, making them the only surviving dinosaurs according to cladistics.[3]");                
        
        anims[9] = new Carnivores(10,"Lions","The lion (Panthera leo) is one of the big cats in the Felidae family and a member of genus Panthera. It has been listed as Vulnerable on the IUCN Red List since 1996, as populations in African range countries declined by about 43% since the early 1990s. Lion populations are untenable outside designated protected areas. Although the cause of the decline is not fully understood, habitat loss and conflicts with humans are the greatest causes of concern.[3] The West African lion population is listed as Critically Endangered since 2016.[5] The only lion population in Asia survives in and around India's Gir Forest National Park and is listed as Endangered since 1986.[6]");
        anims[10] = new Carnivores(11,"Crocodiles","Crocodiles (subfamily Crocodylinae) or true crocodiles are large aquatic reptiles that live throughout the tropics in Africa, Asia, the Americas and Australia. Crocodylinae, all of whose members are considered true crocodiles, is classified as a biological subfamily. A broader sense of the term crocodile, Crocodylidae that includes Tomistoma, is not used in this article. The term crocodile here applies to only the species within the subfamily of Crocodylinae. The term is sometimes used even more loosely to include all extant members of the order Crocodilia, which includes the alligators and caimans (family Alligatoridae), the gharial and false gharial (family Gavialidae), and all other living and fossil Crocodylomorpha.");
        anims[11] = new Carnivores(12,"Sharks","Sharks are a group of elasmobranch fish characterized by a cartilaginous skeleton, five to seven gill slits on the sides of the head, and pectoral fins that are not fused to the head. Modern sharks are classified within the clade Selachimorpha (or Selachii) and are the sister group to the rays. However, the term \"shark\" has also been used for extinct members of the subclass Elasmobranchii outside the Selachimorpha, such as Cladoselache and Xenacanthus, as well as other Chondrichthyes such as the holocephalid eugenedontidans. Under this broader definition, the earliest known sharks date back to more than 420 million years ago.[1] Acanthodians are often referred to as \"spiny sharks\"; though they are not part of Chondrichthyes proper, they are a paraphyletic assemblage leading to cartilaginous fish as a whole.");
        anims[12] = new Carnivores(13,"Otters","Otters are carnivorous mammals in the subfamily Lutrinae. The 13 extant otter species are all semiaquatic, aquatic or marine, with diets based on fish and invertebrates. Lutrinae is a branch of the weasel family Mustelidae, which also includes badgers, honey badgers, martens, minks, polecats, and wolverines.");
        anims[13] = new Carnivores(14,"Weasels","A weasel /ˈwiːzəl/ is a mammal of the genus Mustela of the family Mustelidae. The genus Mustela includes the least weasels, polecats, stoats, ferrets, and minks. Members of this genus are small, active predators, with long and slender bodies and short legs. The family Mustelidae (which also includes badgers, otters, and wolverines) is often referred to as the \"weasel family\". In the UK, the term \"weasel\" usually refers to the smallest species Mustela nivalis.[1]");
        
        //for (Animal anims1 : anims) {
        //    anims1.feedMe("plants");
        //}
// initiate RAM directory
        Directory dir= new RAMDirectory();
// initiate standard analyzer with lucene4.1
        Analyzer analyzer = new StandardAnalyzer(LUCENE_41);
// initiate IndexWriterConfig with lucene4.1 and analyzer
        IndexWriterConfig cfg= new IndexWriterConfig(LUCENE_41,analyzer);
// initiate IndexWriterConfig with lucene4.1 and IndexWriterConfig
        IndexWriter writer = new IndexWriter(dir, cfg);
        
        // generate new fields to be stored in documents
        LongField count = new LongField("count", 0L, Field.Store.YES);
        IntField age = new IntField("age", (int) 0L, Field.Store.YES);
        TextField name = new TextField("name", "A", Field.Store.YES);
        TextField desc = new TextField("desc", "B", Field.Store.YES);
        
        TextField klas = new TextField("klas", "C", Field.Store.YES);
        TextField diet = new TextField("diet", "D", Field.Store.YES);
// create new document
        Document doc = new Document();
// add above defined fields
        doc.add(count);
        doc.add(age);
        doc.add(name);
        doc.add(desc);
        doc.add(klas);
        doc.add(diet);

// loop through each animal and cast its info from array to document
        for(int i = 0; i < 14; i++) {
            count.setLongValue(i);
            age.setIntValue(anims[i].age);
            name.setStringValue(anims[i].name);
            desc.setStringValue(anims[i].desc);
            klas.setStringValue(anims[i].getClass().toString());
            diet.setStringValue(anims[i].feedMe("plant"));
// write document                
            writer.addDocument(doc);
        }
// push document                
        writer.commit();
// close writer
        writer.close();
// define RAM directory for index to read
        IndexReader ir = DirectoryReader.open(dir);
// define IndexSearcher with directory as argument
        IndexSearcher searcher = new IndexSearcher(ir);
//Query q = new TermQuery( new Term("field3","Elephants"));
//create funtion to read users query        
        Scanner reader = new Scanner(System.in);
        System.out.println("Type the query:");

        String q = reader.nextLine();
//adjust multiple fields querying          
        String special = "name:" + q + " OR desc:" + q + " OR klas:" + q;
//create QueryParser        
        QueryParser queryParser = new QueryParser(LUCENE_41,"name", analyzer);
//TopDocs top = searcher.search(q, 10); // perform a query and limit results number
//parse and search the query
        TopDocs top = searcher.search(queryParser.parse(special), 20); // perform a query and limit results number
        ScoreDoc[] hits = top.scoreDocs; // get only the scored documents (ScoreDoc is a tuple)
        Document doc1=null;
//print out number of documents returned
        System.out.println("Returned documents: " + hits.length);
//for each returned document print out its fields
        for(ScoreDoc entry:hits){
            doc1 = searcher.doc(entry.doc); /* the same as ir.document(entry.doc); */
            // System.out.println("count: "+doc1.get("count"));
            System.out.println("age: "+doc1.get("age"));
            System.out.println("name: "+doc1.get("name"));
            System.out.println("desc: "+doc1.get("desc"));
            System.out.println("klas: "+doc1.get("klas"));
            System.out.println("diet: "+doc1.get("diet"));

        }
    }
}
