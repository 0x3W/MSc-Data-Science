/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 *
 * @author Dovla
 */
//initiate class for Herbivores animals that extends main class

class Herbivores extends Animal
{
        //pass Animal variables with "super" command
    public Herbivores (int age, String name, String desc) 
    {
        super(age, name, desc);
    }
        // create a feedMe method
    @Override
    public String feedMe(String food)
    {
        if(food == "plants")
            return "This animal feeds on plants";
        else
            return "This animal does not feed on plants";
    }
}
