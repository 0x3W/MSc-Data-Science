/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * @author Dovla
 *
 */
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.StringField;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;

import java.io.*;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.document.IntField;
import org.apache.lucene.document.LongField;
import org.apache.lucene.index.Term;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.TermQuery;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.RAMDirectory;
import static org.apache.lucene.util.Version.LUCENE_41;


    public abstract class Animal {

        public int age;
        public String name; 
        public String desc;
        
        public Animal(int age, String name, String desc)
        {
            this.age = age;
            this.name = name;
            this.desc = desc;

        }
        public static void main(String[] args) throws IOException {
                
        Animal[] anims;
        anims = new Animal[14];

        anims[0] = new Herbivores(1,"Elephants","A");
        anims[1] = new Herbivores(2,"Rabbits","B");
        anims[2] = new Herbivores(3,"Manatees","C");
        anims[3] = new Herbivores(4,"Deer","D");
        
        anims[4] = new Omnivores(5,"Humans","E");
        anims[5] = new Omnivores(6,"Bears","F");
        anims[6] = new Omnivores(7,"Lemurs","G");
        anims[7] = new Omnivores(8,"Raccoons","H");
        anims[8] = new Omnivores(9,"Birds","I");                
        
        anims[9] = new Carnivores(10,"Lions","K");
        anims[10] = new Carnivores(11,"Crocodiles","L");
        anims[11] = new Carnivores(12,"Sharks","M");
        anims[12] = new Carnivores(13,"Otters","N");
        anims[13] = new Carnivores(14,"Weasels","O");
        
        Directory dir= new RAMDirectory();
        Analyzer analyzer = new StandardAnalyzer(LUCENE_41);

        IndexWriterConfig cfg= new IndexWriterConfig(LUCENE_41,analyzer);
        IndexWriter writer = new IndexWriter(dir, cfg);
        

