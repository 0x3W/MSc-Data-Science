/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Dovla
 */
//initiate class for Omnivore animals that extends main class
class Omnivores extends Animal 
{
    //pass Animal variables with "super" command
    public Omnivores (int age, String name, String desc) 
    {
        super(age, name, desc);
    }
    // create a feedMe method
    @Override
    public String feedMe(String food)
    {
        if(food == "plants")
            return "This animal feeds on plants and meat ";
        else
            return "This animal does not feed on " + food;
    }
}
