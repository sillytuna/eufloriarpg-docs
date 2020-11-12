
Key Class
=========



Namespace
    :dn:ns:`Clay.Game.Mod.Entities`

Assemblies
    * Clay.Game

----

.. contents::
   :local:



Inheritance Hierarchy
---------------------

* :dn:cls:`System.Object`
* :dn:cls:`Tuna.Mob`
* :dn:cls:`Clay.Game.Mod.Entities.Entity`
* :dn:cls:`Clay.Game.Mod.Entities.Vehicle`
* :dn:cls:`Clay.Game.Mod.Entities.Equipment`
* :dn:cls:`Clay.Game.Mod.Entities.Key`




Syntax
------

.. code-block:: csharp

    public class Key : Equipment, IComparable, IAudioSourceInfo, ITargettable, IPathFindingAgent, IProjectileCompatibleEntity





.. dn:class:: Clay.Game.Mod.Entities.Key
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Key


Constructors
------------

.. dn:class:: Clay.Game.Mod.Entities.Key
    :noindex:
    :hidden:

    .. dn:constructor:: Clay.Game.Mod.Entities.Key.Key()




        .. code-block:: csharp

            public Key()



Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.Key
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.Key.ProjectileToCreate



        :rtype: System.String

        .. code-block:: csharp

            public string ProjectileToCreate { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Key._projectile



        :rtype: System.String

        .. code-block:: csharp

            public string _projectile { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Key._tag



        :rtype: System.String

        .. code-block:: csharp

            public string _tag { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Key.isFlower



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isFlower { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Key.isTargetable



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isTargetable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Key.projectile



        :rtype: KeyProjectile

        .. code-block:: csharp

            public KeyProjectile projectile { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Key.spawnHeader



        :rtype: System.String

        .. code-block:: csharp

            public override string spawnHeader { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Key.useSpawnEntityCommand



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool useSpawnEntityCommand { get; }



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Key
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Key.CloneConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            public override void CloneConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.Key.Deactivate(System.Boolean)



        :type quietly: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool Deactivate(bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.Key.EntityFixedUpdate(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void EntityFixedUpdate(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Key.InitialiseApp()




        .. code-block:: csharp

            public static void InitialiseApp()

    .. dn:method:: Clay.Game.Mod.Entities.Key.InitialiseLevel()




        .. code-block:: csharp

            public static void InitialiseLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Key.ParentColonised()




        .. code-block:: csharp

            public override void ParentColonised()

    .. dn:method:: Clay.Game.Mod.Entities.Key.SetTree(Clay.Game.Mod.Entities.Flora)



        :type tree: Clay.Game.Mod.Entities.Flora


        .. code-block:: csharp

            public void SetTree(Flora tree)

    .. dn:method:: Clay.Game.Mod.Entities.Key.SpawnFlower(System.String[])



        :type parameters: System.String<System.String>[]

        :rtype: Clay.Game.Mod.Entities.Key

        .. code-block:: csharp

            public static Key SpawnFlower(string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Key.SpawnFlowerLua(System.String)



        :type parameters: System.String

        :rtype: Clay.Game.Mod.Entities.Key

        .. code-block:: csharp

            public static Key SpawnFlowerLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Key.SpawnKey(System.String[])



        :type parameters: System.String<System.String>[]

        :rtype: Clay.Game.Mod.Entities.Key

        .. code-block:: csharp

            public static Key SpawnKey(string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Key.SpawnKeyLua(System.String)



        :type parameters: System.String

        :rtype: Clay.Game.Mod.Entities.Key

        .. code-block:: csharp

            public static Key SpawnKeyLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Key.Trashed()




        .. code-block:: csharp

            public override void Trashed()

    .. dn:method:: Clay.Game.Mod.Entities.Key.Update(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void Update(float time)



Fields
------

.. dn:class:: Clay.Game.Mod.Entities.Key
    :noindex:
    :hidden:

    .. dn:field:: Clay.Game.Mod.Entities.Key.collectSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public static float collectSpeed



