package com.sd.agenda.interfaces

import com.sd.agenda.pojo.Person

/**
 * @author Timofti Gabriel
 */
interface AgendaService {
    fun getPerson(id: Int) : Person?
    fun createPerson(person: Person)
    fun deletePerson(id: Int)
    fun updatePerson(id: Int, person: Person)
    fun searchAgenda(lastNameFilter: String, firstNameFilter: String, telephoneNumberFilter: String): List<Person>
}